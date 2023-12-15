from fastapi import FastAPI, Depends
import uvicorn

from pydantic import BaseModel

from src.config import load_config
from src.model import Model
from src.embeddings import Embeddings
from src.text_processing import TextProcessing
from src.vector_store import VectorStore
from src.qa_chain import QAChain

app = FastAPI()

class Item(BaseModel):
    input_query: str

@app.post("/chat")
def run(item: Item):
    return qa_chain.get_response(item.input_query)

def setup():
    global qa_chain
    config = load_config('conf/variables.yaml')
    model = Model(config['model_id'])
    embeddings = Embeddings(config['embeddings_model_name'])
    text_processor = TextProcessing(config['pdf_files'])
    texts = [chunk for chunks in text_processor.process_text() for chunk in chunks]
    vector_store = VectorStore(texts, embeddings.embeddings)
    qa_chain = QAChain(model.llm, config['chain_type'], vector_store.vector_store)

if __name__ == "__main__":
    setup()
    uvicorn.run(app, host="0.0.0.0", port=8000)