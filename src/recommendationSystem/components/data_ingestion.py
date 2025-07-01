import os
import sys

from recommendationSystem.logging import logger
from recommendationSystem.utils.common import CustomException
from recommendationSystem.config.configuration import DataIngestionConfig

import pandas as pd

#from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
 
        logger.info("Entered the Data Ingestion method")


        try:
            # Importing Data
            #df_info = pd.read_csv('data/anime_data_24.csv')
            #df_links = pd.read_csv('data/anime_links.csv')
            anime = pd.read_csv(os.path.join("data","anime_data_7490.csv"))
            logger.info("Read the dataset as a dataframe")

            # Making Directory to store the data
            os.makedirs(os.path.dirname(self.ingestion_config.data_path),exist_ok=True)
            logger.info("created directory for datframe")
            
            # Merging the dataset
            #anime = df_info.merge(df_links,on='name')

            # Selecting the required columns
            #anime = anime[['name','sypnopsis','image','type','episodes','status','studios','source','genres','demographic','links']]
            #anime.dropna(inplace=True)
            #logger.info("Filtered out necessary columns and dropped NA rows")

            # Formatting the data to get clean data
            #anime['sypnopsis_length'] = [len(i) for i in anime.sypnopsis]
            #anime = anime[anime['sypnopsis_length'] > 300]
            anime['tags'] = anime['sypnopsis']+" " + anime['type']+" " + anime['episodes']+" " \
               + anime['status'] +" "+ anime['studios'] +" "+ anime['source']+" " + anime['genres']+" " + anime['demographic']   

            # Saving the clean data py
            anime.to_csv(self.ingestion_config.data_path,index=False,header=True)
            logger.info("Ingestion is completed")
            logger.info("---------------x DIRECTORY CHANGE x------------------")


            return(
                self.ingestion_config.data_path
            )

        except Exception as e:
            raise CustomException(e,sys)