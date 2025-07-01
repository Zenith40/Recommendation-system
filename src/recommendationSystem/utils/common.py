# --------------------------------- CUSTOM EXCEPTION CLASS --------------------------------------------

# Importing Libraries
import sys  


# Defining structure of exception message
def error_message_detail(error:Exception,error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    line_number = exec_tb.tb_lineno
    error_message = f"Error occured in python script name [{file_name}] " \
        f"line number [{line_number}] error message [{error}]"
    return error_message

# Getting the exception message from sys
class CustomException(Exception):
    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    




# --------------------------------- PREPROCESSING THE TEXT IN THE DATAFRAME --------------------------------------------

# Importing Libraries
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def removing_blank_lines(text):
    return text.replace('\n'," ")

def removing_pre_suff_ix(text):
    y = []
    
    for i in text.split():
        y.append(PorterStemmer().stem(i))
    
    return " ".join(y)

def converting_into_vectors(text):
    vec = CountVectorizer(max_features=5000,stop_words='english').fit_transform(text).toarray()
    return vec

def finding_similarity(vec):
    similarity = cosine_similarity(vec)
    return similarity

# --------------------------------- SAVING FILES --------------------------------------------

import os
import dill

from recommendationSystem.logging import logger


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    

# --------------------------------- Prediction File --------------------------------------------

import numpy as np

def recommend(data,matrix,anime):
    anime_index = data[data.title == anime].index[0]
    distances = np.around(matrix[anime_index],2)
    anime_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[0:10]

    recommended_anime = []
    recommended_anime_poster = []
    recommended_anime_link = []
    recommended_similarity_score = []

    for i in anime_list:
        # anime
        recommended_anime.append(data.iloc[i[0]].title)
        # posters
        recommended_anime_poster.append(data.iloc[i[0]].image)
        # links
        recommended_anime_link.append(data.iloc[i[0]].links)
        # score
        recommended_similarity_score.append(f'{np.around(i[1]*100,2)} %')
    return recommended_anime, recommended_anime_poster, recommended_anime_link, recommended_similarity_score

# --------------------------------- Find Story of the anime --------------------------------------------

import pandas as pd

def find_anime(label):
    dataframe_path = os.path.join("artifact","data.csv")
    df = pd.read_csv(dataframe_path)
    story = '\n'.join(df[df.name == label].sypnopsis.to_list())
    return story


