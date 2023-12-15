from langchain.vectorstores import FAISS

class VectorStore:
    def __init__(self, texts, embeddings):
        self.vector_store = FAISS.from_texts(texts, embedding=embeddings)