import streamlit as st
import pandas as pd
import pickle

#------------------------------------RAG BASED CHATBOT ---------------------------------------

from recommendationSystem.chatbot.client_module.utils import chatbot

chatbot()
#render_history_download()

#----------------------------------- RECOMMEDATION SYSTEM -----------------------------------------

from utils import fetch_transformed_data, anime_info
 
st.title("Anime Recommender System")

data_path, matrix_path = fetch_transformed_data()

anime_data = pd.read_csv(data_path)
similarity_matrix = pickle.load(open(file=matrix_path,mode='rb'))

select_anime_name = st.selectbox(
    "Choose Anime Name : ",
    anime_data['title'].values,
    index=None,
    placeholder="Select the anime for recommendation..."
)

anime_info(anime_name=select_anime_name,anime_data=anime_data,similarity_matrix=similarity_matrix)
