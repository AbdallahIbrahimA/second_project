import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import pickle

def save_object(file_path:str , obj):
    try:
        # creating dirname component to be able to create the directory using os package 
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path , 'wb') as file_obj:
            # making the pkl file using pickle package
            pickle.dump(obj,file_obj)

    
    except Exception as e :
        raise CustomException(e,sys)
