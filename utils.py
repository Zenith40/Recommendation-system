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


# --------------------------------------------------------------------------------------------

def chatbot():
    with st.sidebar:

        # Input and response
        user_input = st.chat_input(placeholder="Ask Anything")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        if user_input:
            #st.chat_message("user").markdown(user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})
        

        # Render existing chat history
        for msg in st.session_state.messages[::-1]:
            st.chat_message(msg["role"]).markdown(msg["content"])

        if user_input:
            answer = " :( ?"
            st.chat_message("assistant").markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content":answer })

        
        