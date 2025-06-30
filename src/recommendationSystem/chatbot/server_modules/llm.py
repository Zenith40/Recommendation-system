import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


def get_llm_chain(vectorstore):
    llm=ChatGroq(
        groq_api_key=api_key,
        model_name="llama3-70b-8192"
    )

    retriever=vectorstore.as_retriever(
        search_kwargs={
            "k":8,
            #"lambda_mult": 0.5
        }
    )


    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )