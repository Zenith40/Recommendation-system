import requests

API_URL = "http://127.0.0.1:8000"

def load_pdfs_api(path):
    return requests.post(f"{API_URL}/load_pdf/",json={"path": path})

def ask_question(question):
    return requests.post(f"{API_URL}/ask/",data={"question":question})