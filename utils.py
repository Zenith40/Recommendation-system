import streamlit as st


from predict_trial import return_data

@st.cache_resource
def fetch_transformed_data():
    with st.spinner("Started training the model...",show_time=True):
        data_path, matrix_path = return_data().predict()
        return data_path,matrix_path
    st.success("Deployment complete, Successfully created the system!")

#-----------------------------------------------------------------------------

from recommendationSystem.utils.common import recommend,find_anime

@st.cache_resource
def anime_info(anime_name,anime_data,similarity_matrix):
    if anime_name is not None:
            st.write('\n\n\n')

            name, posters, link, score = recommend(data=anime_data,matrix=similarity_matrix,anime=anime_name)

            _, col, _ = st.columns(3)

            with col:
                st.image(posters[0])

            st.text(f"{find_anime(anime_name)}")
            st.write(f'Similarity Score : {score[0]}')
            st.write('')
            st.link_button("Know More", link[0],use_container_width=True)

            for i in range(1,9,3):
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.image(posters[i])
                    st.write(name[i])
                    st.write(f'Similarity Score : {score[i]}')
                    st.write('')
                    st.link_button("Know More", link[i],use_container_width=True)

                with col2:
                    st.image(posters[i+1])
                    st.write(name[i+1])
                    st.write(f'Similarity Score : {score[i+1]}')
                    st.write('')
                    st.link_button("Know More", link[i+1],use_container_width=True)

                with col3:
                    st.image(posters[i+2])
                    st.write(name[i+2])
                    st.write(f'Similarity Score : {score[i+2]}')
                    st.write('')
                    st.link_button("Know More", link[i+2],use_container_width=True)

                st.write('\n\n\n')



# --------------------------------------- CHATBOT------------------------------------------------


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


