import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

texts=[
    "Machine learning is amazing",
    "Deep learning is a subset of machine learning",
    "FAISS is great for searching similar items",
    "Python is a popular programming language"
]

embeddings = model .encode(texts)
embeddings = np.array(embeddings, dtype=np.float32)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

query_text = input("Enter your search query:")
query_embedding = model.encode([query_text]).astype(np.float32)

D, I = index.search(query_embedding, 2)

print("\n🔍 **Search Results:**")
print(f"Query: {query_text}")
print(f"Top Match 1: {texts[I[0][0]]} (Distance: {D[0][0]:.4f})")
print(f"Top Match 2: {texts[I[0][1]]} (Distance: {D[0][1]:.4f})")