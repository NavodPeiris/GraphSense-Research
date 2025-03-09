import faiss
import numpy as np
from gensim.models import FastText

# Load trained FastText model (used only once to save vectors)
model = FastText.load("large_model/graph_embeddings.model")

# Extract word vectors & words
words = np.array(model.wv.index_to_key)  # List of words
vectors = np.array([model.wv[word] for word in words], dtype=np.float32)  

# Save FAISS index
index = faiss.IndexFlatL2(vectors.shape[1])  # L2 distance search
index.add(vectors)  
faiss.write_index(index, "faiss_index.bin")

# Save words and word-vector mapping
np.save("word_list.npy", words)
np.save("word_vectors.npy", vectors)  # Store word vectors separately

print("FAISS index and word-vector mapping saved!")
