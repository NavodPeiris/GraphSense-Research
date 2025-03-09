import psutil
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
    print(similar_lines)
    

# Lists to store memory usage and timestamps
memory_usage = []
timestamps = []
execution_times = []
execution_time = 0
consumed_memory = 0

if __name__ == "__main__":
    process = psutil.Process(os.getpid())
    before = process.memory_info().rss
    
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

    for i in range(10):
        # Start measuring time
        start_time = time.time()
        infer_graph_model_faiss("for src,des in required_edges:")
        # Calculate execution time
        exec_time = round(time.time() - start_time, 4)
        execution_time = execution_time + exec_time
        after = process.memory_info().rss
        mem = round((after - before) / 10**6, 4)
        consumed_memory = consumed_memory + mem

        timestamps.append(i + 1)  # Iteration number as timestamp
        memory_usage.append(mem)
        execution_times.append(exec_time)

    print(f"average memory usage: {round(consumed_memory/10, 4)} MB")
    print(f"average execution time: {round(execution_time/10, 4)} seconds")

    # Plot memory usage
    plt.figure(figsize=(8, 5))
    plt.plot(timestamps, memory_usage, marker='o', linestyle='-', color='b', label='Memory Usage (MB)')
    plt.xlabel("Iteration")
    plt.ylabel("Memory Used (MB)")
    plt.title("Memory Usage Over Iterations")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot execution time
    plt.figure(figsize=(8, 5))
    plt.plot(timestamps, execution_times, marker='o', linestyle='-', color='b', label='Execution Time (s)')
    plt.xlabel("Iteration")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time Over Iterations")
    plt.legend()
    plt.grid(True)
    plt.show()