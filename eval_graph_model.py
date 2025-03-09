import os
import time
import matplotlib.pyplot as plt
import faiss
import numpy as np
import struct
from rocksdbpy import Option
import rocksdbpy
import pickle
from light_embed import TextEmbedding

index = None
idx_to_line = None
line_to_idx = None
txt_embed_index = None
txt_embed_model = None
loaded_pca = None

# Function to track execution time and peak RAM usage
def infer_graph_model_faiss(line, top_k=10):
    query_index = None
    top_k = top_k + 1 # top vector is always same vector so we remove it
    idx_bytes = line_to_idx.get(line.encode())

    if idx_bytes:
        query_index = struct.unpack("i", idx_bytes)[0]  # Unpack the 4-byte integer
        print(f"Index: {query_index}")
    else:
        print("Line not found")
        # handle OOV
        oov_vector = txt_embed_model.encode(line)
        # Reshape to (1, dim), Faiss expects a 2D array for a single query
        oov_vector = np.expand_dims(oov_vector, axis=0)

        oov_vector = loaded_pca.transform(oov_vector) # reduce dimensions to 128
        
        oov_vector = oov_vector.astype(np.float16)

        # Perform FAISS search
        distances, indices = txt_embed_index.search(oov_vector, 1)
        # Retrieve syntactically matching line
        matched_line = idx_to_line.get(struct.pack("i", indices[0][0])).decode()
        print("oov matched to: ", matched_line)
        query_index = indices[0][0]
        query_index = int(query_index)
        print(f"Matched Index: {query_index}")
    
    # Load vector dynamically using index to minimize memory usage
    query_vector = np.array([index.reconstruct(query_index)], dtype=np.float16)  # Dynamically load vector using FAISS
    
    # Perform FAISS search
    distances, indices = index.search(query_vector, top_k)

    # Retrieve similar lines using direct indexing
    similar_lines = [idx_to_line.get(struct.pack("i", idx)).decode() for idx in indices[0]]
    similar_lines = similar_lines[1:]   # remove top vector as it is same as query vector
    return similar_lines
    

# Lists to store memory usage and timestamps
memory_usage = []
timestamps = []
execution_times = []
execution_time = 0
consumed_memory = 0

test_lines = []
correct_next_lines = []

if __name__ == "__main__":
    index = faiss.read_index("artifacts/faiss_index.bin")

    opts = Option()
    opts.create_if_missing(False)

    line_to_idx = rocksdbpy.open('artifacts/line_to_idx.db', opts)
    idx_to_line = rocksdbpy.open('artifacts/idx_to_line.db', opts)
    txt_embed_index = faiss.read_index("artifacts/faiss_txt_embed_index.bin")
    txt_embed_model = TextEmbedding('onnx-models/all-MiniLM-L6-v2-onnx')  # embed text for OOV handling

    try:
        with open('artifacts/pca_model.pkl', 'rb') as file:
            loaded_pca = pickle.load(file)
    except FileNotFoundError:
        print("The PCA model file was not found. Ensure it is available for OOV handling")

    edg_file_path = "output_dataset.edg"  # Change this to your actual file path

    # Read the .edg file and parse the values
    with open(edg_file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("‖")  # Split using the delimiter
            if len(parts) >= 2:
                test_lines.append(parts[0])  # Current line
                correct_next_lines.append(parts[1])  # Next line

    print(f"Loaded {len(test_lines)} test lines and {len(correct_next_lines)} correct next lines.")

    top1_score = 0
    top3_score = 0
    top10_score = 0

    for i in range(len(test_lines)):
        similar_lines = infer_graph_model_faiss(test_lines[i])
        correct_next_line = correct_next_lines[i]
        for j in range(len(similar_lines)):
            if(similar_lines[j] == correct_next_line):
                if j == 0:  # Top 1
                    top1_score += 1
                    top3_score += 1
                    top10_score += 1
                elif j <= 2:  # Top 3
                    top3_score += 1
                    top10_score += 1
                elif j <= 9:  # Top 10
                    top10_score += 1
                break
    
    print("top-1 accuracy = ", top1_score / len(test_lines))
    print("top-3 accuracy = ", top3_score / len(test_lines))
    print("top-10 accuracy = ", top10_score / len(test_lines))