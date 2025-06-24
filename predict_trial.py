import sys
#import pandas as pd
#import pickle
import os

from recommendationSystem.components.data_ingestion import DataIngestion
from recommendationSystem.components.data_transformation import DataTransformation
from recommendationSystem.utils.common import CustomException

class return_data:
    def __init__(self):
        pass

    def predict(self):
        try:
            obj = DataIngestion().initiate_data_ingestion()
            matrix_path, data_path = DataTransformation().initiate_data_transformation_obj(obj)
            return matrix_path,data_path

        except Exception as e:
            raise CustomException(e,sys)