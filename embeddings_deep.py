from langchain_openai.embeddings import OpenAIEmbeddings
import numpy as np
from dotenv import load_dotenv

load_dotenv()

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

def basic_embeddings():

    text= "What is deep learning?"
    single_embedding = embeddings_model.embed_query(text)
    print(f"Vendor Dimensions: {len(single_embedding)}")
    print(f"First 5 values: {single_embedding[:5]}")
    
    # Calculate vector norm

    print(f"Vector Norm: {np.linalg.norm(single_embedding):.4f}")

def batch_embeddings():
    text = [
        "What is Machine Learning?",
        "Explain the concept of overfitting in ML.",
        "How does a neural network work?",
    ]

    batch_embedding = embeddings_model.embed_documents(text)
    for i, emb in enumerate(batch_embedding):
        print(f"Text {i+1} - Vector dimensions: {len(emb)}")
        print(f"Text {i+1} - First 5 values: {emb[:5]}")
        print(f"Text {i+1} - Vector norm: {np.linalg.norm(emb):.4f}")


# similarity search
# embedding_caching

if __name__ == "__main__":
    # basic_embeddings()
    batch_embeddings()