import os
import sys
from exception import CustomException
from logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# DataIngestionConfig is to configure the data-source path and path where we store data 'artifacts'
# for best practices we should have another folder config_entity for all the configurations of the project 
# @dataclass allows you to directly define the class variables. but if you will use othe functions then just don't use it
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    # In this method we read the data from its source and save raw, train and test data and we return the paths for train and test data
    # reads data from it's source. For best practices it's better if the method to do so is written in utils.py and only used here
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df = pd.read_csv("D:\\CAREER\\DL Courses\\end-to-end-ml-project\\notebook\\data\\stud.csv")
            logging.info("Data has been read successfully")

            #This next line of code creates the folder the will contain the ingested data
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()


