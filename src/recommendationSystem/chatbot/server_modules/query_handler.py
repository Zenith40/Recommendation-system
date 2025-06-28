# Query Chain

def query_chain(chain,user_input:str):
  result = chain({"query": user_input})
  response = {
      "response":result["result"],
      "sources":[doc.metadata.get('source','') for doc in result["source_documents"]]
      }
  return response