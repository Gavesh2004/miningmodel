from langchain.embeddings import HuggingFaceEmbeddings

class Embeddings:
    def __init__(self, model_name):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)