import streamlit as st
import os

def cache_clear(x):
    if st.sidebar.button("Reset Chat History",use_container_width=True):
        x.clear()

#from recommendationSystem.chatbot.client_module.api import ask_question
from recommendationSystem.chatbot.server_modules.llm import get_llm_chain
from recommendationSystem.chatbot.server_modules.load_vector_store import use_vectorstore
from recommendationSystem.chatbot.server_modules.query_handler import query_chain


def chatbot():
    vectorstore = use_vectorstore()
    chain = get_llm_chain(vectorstore)
    url = "https://raw.githubusercontent.com/Zenith40/Recommendation-system/refs/heads/main/data/anime_data_7490.txt"

    if "messages" not in st.session_state:
            st.session_state.messages = []
            
    with st.sidebar:
        
        st.title("🍥 RARE AT YOUR SERVICE ")
        st.write("RAG-based Anime Recommendation Engine")

        # Input and response
        user_input = st.chat_input(placeholder="Ask Anything")
        cache_clear(st.session_state.messages)
        
        if user_input:
            #response = ask_question(user_input)
            #if response.status_code == 200:
            response=query_chain(chain,user_input=user_input)
            #data = response.json()
            answer = response["response"]
            #sources = response.get("sources",[])
            #st.chat_message("assistant").markdown(answer)
            st.session_state.messages.insert(0,{"role": "assistant", "content": answer})
            st.session_state.messages.insert(0,{"role": "user", "content": user_input})
            st.markdown(f"📄 Source : [Anime_Data.txt](%s)" %url)
            #else:
                #st.error(f"Error: {response.text}")

            # Render existing chat history
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).markdown(msg["content"])
         

# History Downloader

def render_history_download():
    if st.session_state.get("message"):
        chat_text="\n\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
        st.download_button("Download Chat History",chat_text,file_name="chat_history.txt",mime="text/plain")


