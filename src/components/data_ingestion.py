import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
# used for creating class variable 
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

@dataclass # easy way of defining attributes in the class
class DataIngestionconfig:
    train_data_path: str = os.path.join("artifacts" , "train.csv")
    test_data_path: str = os.path.join("artifacts" , "test.csv")
    raw_data_path: str = os.path.join("artifacts" , "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig() 
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")
            
            # saving the data in it's corresponding path 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("train test split is intiated")
            train_set , test_set = train_test_split(df,test_size=.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                # self.ingestion_config.raw_data_path,
            )

        except Exception as e:
            raise CustomException(e,sys)
    
