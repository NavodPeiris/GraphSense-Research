import umap
import matplotlib.pyplot as plt
import plotly.express as px
from gensim.models import Word2Vec
import numpy as np

# Load the saved Node2Vec model
model = Word2Vec.load('graph_embeddings.model')

# Extract the node embeddings
node_embeddings = []
node_labels = []

# Assuming node labels are the keys of the model's vocabulary
for node in model.wv.index_to_key:
    node_embeddings.append(model.wv[node])
    node_labels.append(node)

# Convert to numpy array
node_embeddings = np.array(node_embeddings)

# Apply UMAP for 2D and 3D visualization
umap_2d = umap.UMAP(n_components=2, random_state=42)
umap_3d = umap.UMAP(n_components=3, random_state=42)

# Fit UMAP
node_embeddings_2d = umap_2d.fit_transform(node_embeddings)
node_embeddings_3d = umap_3d.fit_transform(node_embeddings)

# 2D Visualization with Matplotlib
plt.figure(figsize=(10, 8))
plt.scatter(node_embeddings_2d[:, 0], node_embeddings_2d[:, 1], s=50, cmap='viridis')
for i, label in enumerate(node_labels):
    plt.annotate(label, (node_embeddings_2d[i, 0], node_embeddings_2d[i, 1]), fontsize=8)
plt.title("Node2Vec Embeddings - 2D Visualization")
plt.xlabel("UMAP Dimension 1")
plt.ylabel("UMAP Dimension 2")
plt.show()

# 3D Visualization with Plotly
fig = px.scatter_3d(
    x=node_embeddings_3d[:, 0], 
    y=node_embeddings_3d[:, 1], 
    z=node_embeddings_3d[:, 2], 
    color=node_labels, 
    labels={'color': 'Node Labels'},
    title="Node2Vec Embeddings - 3D Visualization"
)
fig.update_traces(marker=dict(size=5))
fig.show()
