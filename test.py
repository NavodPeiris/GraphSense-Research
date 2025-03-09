from gensim.models import Word2Vec
import os
import psutil
import joblib
import faiss
import numpy as np
from rocksdbpy import Option
import rocksdbpy
import struct
import numpy as np
from sklearn.decomposition import PCA
import pickle
from light_embed import TextEmbedding
import sys

# Function to delete the RocksDB database if it exists
def delete_db_if_exists(db_path):
    if os.path.exists(db_path):
        print(f"Deleting existing database at {db_path}")
        # Remove the database directory (RocksDB stores files in a folder)
        os.remove(db_path)

os.makedirs("artifacts", exist_ok=True)

try:
    # Delete the existing databases if they exist
    delete_db_if_exists("artifacts/line_to_idx.db")
    delete_db_if_exists("artifacts/idx_to_line.db")
except Exception as err:
    print("Permission Denied: please delete folders artifacts/line_to_idx.db and artifacts/idx_to_line.db manually")
    sys.exit(1)

txt_embed_model = TextEmbedding('onnx-models/all-MiniLM-L6-v2-onnx')  # embed text for OOV handling

model = Word2Vec.load("small_model/graph_embeddings.model")

# Load the full vectors
line_vectors = model.wv.vectors

# Get total vocabulary size
total_lines = len(line_vectors)

print(f"Total code lines in vocabulary: {total_lines}")

# Select the top N most frequent lines
top_n = 1000000
top_lines = model.wv.index_to_key[:top_n]

# Create a list of vectors for FAISS
vectors = []
opts = Option()
opts.create_if_missing(True)

line_to_idx = rocksdbpy.open('artifacts/line_to_idx.db', opts)
idx_to_line = rocksdbpy.open('artifacts/idx_to_line.db', opts)

idx = 0
for line in top_lines:
    vector = line_vectors[model.wv.key_to_index[line]]
    line_to_idx.set(line.encode(), struct.pack("i", idx))
    idx_to_line.set(struct.pack("i", idx), line.encode())
    vectors.append(vector)
    idx += 1

# Convert the list of vectors into a NumPy array
vectors_for_faiss = np.array(vectors, dtype=np.float16)

print(vectors_for_faiss.shape)

# Create a FAISS index (for example, using L2 distance)
index = faiss.IndexFlatL2(vectors_for_faiss.shape[1])  # Using L2 distance
index = faiss.IndexScalarQuantizer(vectors_for_faiss.shape[1], faiss.ScalarQuantizer.QT_fp16)

# Add vectors to the FAISS index
index.add(vectors_for_faiss)

# Save the FAISS index
faiss.write_index(index, 'artifacts/faiss_index.bin')

# generate text embeddings for OOV handling
txt_embeddings = txt_embed_model.encode(top_lines)

if txt_embeddings.shape[0] > vectors_for_faiss.shape[1]:
    # Reduce the dimensionality to 128 dimensions using PCA
    pca = PCA(n_components=vectors_for_faiss.shape[1])
    reduced_txt_embeddings = pca.fit_transform(txt_embeddings)
    # Save the PCA model for dimensionality reduction
    with open('artifacts/pca_model.pkl', 'wb') as file:
        pickle.dump(pca, file)
    txt_embeddings_for_faiss = reduced_txt_embeddings.astype(np.float16)
else:
    txt_embeddings_for_faiss = txt_embeddings.astype(np.float16)

print(txt_embeddings_for_faiss.shape)

# Create a FAISS index for txt embeddings
txt_embed_index = faiss.IndexFlatL2(txt_embeddings_for_faiss.shape[1])  # Using L2 distance
txt_embed_index = faiss.IndexScalarQuantizer(txt_embeddings_for_faiss.shape[1], faiss.ScalarQuantizer.QT_fp16)

# Add vectors to the FAISS index
txt_embed_index.add(txt_embeddings_for_faiss)

# Save the FAISS index
faiss.write_index(txt_embed_index, 'artifacts/faiss_txt_embed_index.bin')


print("FAISS index and RocksDB stores saved successfully!")