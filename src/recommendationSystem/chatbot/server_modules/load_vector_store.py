import os
#from pathlib import Path
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
#from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



# Initializing Directories

save_path = os.path.join("chromadb")
#os.makedirs(save_path, exist_ok=True)

def load_vectorstore(pdf_path):

  # Loading the doc
  #docs = []
  #loader = PyPDFLoader(pdf_path)
  #docs.extend(loader.load())

  #Spliiting the data into smaller chunks
  #splitter = RecursiveCharacterTextSplitter( chunk_size=10, chunk_overlap=1000)
  #chunks = splitter.split_documents(docs)
  text_path = os.path.join("data","anime_data_7490.txt")

  with open(text_path, "r", encoding="utf-8") as f:
    text = f.read()

  #Spliiting the data into smaller chunks
  splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=150,
    separators=["\n\n\n\n","\n","."]
  )
  chunks = splitter.split_text(text)

   # Coverting the text into numerical value
  embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/e5-large-v2",
    #model_kwargs={'device': 'cuda'},     # if using GPU
    encode_kwargs={'batch_size': 32, 'normalize_embeddings': True}
  )
    
     # Check if vectorstore already exists
  if os.path.exists(save_path) and os.listdir(save_path):
    # Load existing vectorstore
    vectorstore = Chroma(persist_directory=save_path, embedding_function=embeddings)
    for i in range(0, len(chunks), 1000):
      chunk_batch = chunks[i:i+1000]
      vectorstore.add_texts(
          chunk_batch,
          ids=[f"chunk-{i+j}" for j in range(len(chunk_batch))]
          )
    vectorstore.persist()

  else:
      # Create new vectorstore from scratch in batches
      all_ids = []
      for i in range(0, len(chunks), 1000):
        chunk_batch = chunks[i:i+1000]
        if i == 0:
            vectorstore = Chroma.from_texts(
              texts=chunk_batch,
              embedding=embeddings,
              persist_directory=save_path
            )
        else:
            vectorstore.add_texts(
              chunk_batch,
              ids=[f"chunk-{i+j}" for j in range(len(chunk_batch))]
            )
      vectorstore.persist()

  return vectorstore

def use_vectorstore(path):
  embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/e5-large-v2",
    #model_kwargs={'device': 'cuda'},     # if using GPU
    encode_kwargs={'batch_size': 32, 'normalize_embeddings': True}
  )

  vectorstore = Chroma(
      persist_directory=path,
      embedding_function=embeddings
  )

  return vectorstore