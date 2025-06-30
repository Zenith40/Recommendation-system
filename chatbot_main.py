from fastapi import FastAPI,File,Form,Request,Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

#import threading
import uvicorn
#import os

from recommendationSystem.chatbot.server_modules.llm import get_llm_chain
from recommendationSystem.chatbot.server_modules.load_vector_store import use_vectorstore
from recommendationSystem.chatbot.server_modules.query_handler import query_chain


app = FastAPI(title='Anime Rag Chatbot')


# allow frontend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class PathInput(BaseModel):
    path: str

@app.middleware("http")
async def catch_exception_middleware(request:Request,call_next):
     return await call_next(request)
    
@app.post("/load_pdf/")
async def loadpdf(data:PathInput):
    use_vectorstore(data.path)
    return {"message":"Files processed and vectorstore updated"}


@app.post("/ask/")
async def ask_question(question:str=Form(...)):
    from langchain.vectorstores import Chroma
    from langchain.embeddings import HuggingFaceBgeEmbeddings
    from recommendationSystem.chatbot.server_modules.load_vector_store import save_path
    
    vectorstore=Chroma(
        persist_directory=save_path,
        embedding_function=HuggingFaceBgeEmbeddings(
            model_name="intfloat/e5-large-v2",
            #model_kwargs={'device': 'cuda'},     # if using GPU
            encode_kwargs={'batch_size': 32, 'normalize_embeddings': True}
        )
    )
    chain=get_llm_chain(vectorstore)
    result=query_chain(chain,question)
    return result

def run_api():
    uvicorn.run(app, host="0.0.0.0", port=8000,reload=False)


