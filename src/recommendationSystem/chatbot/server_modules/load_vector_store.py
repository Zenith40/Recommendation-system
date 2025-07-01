from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import os

save_path = os.path.join("chromadb")

def use_vectorstore():
  
  embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/e5-large-v2",
    #encode_kwargs={'batch_size': 32, 'normalize_embeddings': True}
  )

  vectorstore = Chroma(
      persist_directory=save_path,
      embedding_function=embeddings
  )

  return vectorstore