from gensim.models import FastText

# Load full FastText model
model = FastText.load("large_model/graph_embeddings.model")

# Save only word vectors (without subword information)
model.wv.save("word_vectors.kv")

print("Saved only word vectors (without subword info).")
