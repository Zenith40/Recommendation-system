import streamlit as st
import os
import time

'''@st.cache_resource
def run_fastapi():
    with st.spinner("Initializing the Fastapi...",show_time=True):
        time.sleep(5)
        os.system("uvicorn chatbot_main:app --reload")
    st.success("Deployment complete, Successfully created the system!")'''

def cache_clear(x):
    if st.sidebar.button("Reset Chat History",use_container_width=True):
        x.clear()

from recommendationSystem.chatbot.client_module.api import ask_question
def chatbot():

    if "messages" not in st.session_state:
            st.session_state.messages = []
            
    with st.sidebar:
        
        st.title("🍥 RARE AT YOUR SERVICE ")
        st.write("RAG-based Anime Recommendation Engine")

        # Input and response
        user_input = st.chat_input(placeholder="Ask Anything")
        cache_clear(st.session_state.messages)
            
        '''if user_input:
            st.chat_message("user").markdown(user_input)'''


        if user_input:
            response = ask_question(user_input)
            if response.status_code == 200:
                data = response.json()
                answer = data["response"]
                sources = data.get("sources",[])
                #st.chat_message("assistant").markdown(answer)
                st.session_state.messages.insert(0,{"role": "assistant", "content": answer})
                st.session_state.messages.insert(0,{"role": "user", "content": user_input})
                st.markdown(f"📄 **Source : {sources[0].split("\\")[-1]}**")
            else:
                st.error(f"Error: {response.text}")

            # Render existing chat history
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).markdown(msg["content"])
        

        

        

# History Downloader

def render_history_download():
    if st.session_state.get("message"):
        chat_text="\n\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
        st.sidebar.download_button("Download Chat History",chat_text,file_name="chat_history.txt",mime="text/plain")


# data loader

from recommendationSystem.chatbot.client_module.api import load_pdfs_api


@st.cache_resource
def render_loader(path):
    response=load_pdfs_api(path)
    if response.status_code==200:
        pass
    else:
        st.sidebar.error(f"Error: {response.text}")