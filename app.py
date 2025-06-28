import streamlit as st
import pandas as pd
import pickle
import os
import threading

from utils import fetch_transformed_data, anime_info
from recommendationSystem.chatbot.client_module.utils import chatbot, render_history_download,render_loader
from chatbot_main import run_api

#---------------------------------------------------------------------------
api_thread = threading.Thread(target=run_api, daemon=True)


path = os.path.join("chromadb_anime_data_7490_e5largev2_1.5K_batch")

#run_fastapi()
api_thread.start()
render_loader(path)
chatbot()
render_history_download()

#----------------------------------------------------------------------------
 
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