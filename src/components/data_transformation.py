import sys
import os
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler, RobustScaler, PowerTransformer, QuantileTransformer, Normalizer, Binarizer

from exception import CustomException
from logger import logging
from utils import save_object


#this is to get the path required for data transformation
# @dataclass allows you to directly define the class variables. but if you will use othe functions then just don't use it
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):

        '''

        This function is responsible for data transformation
        
        '''
        try:
            
            numerical_columns = [
                'reading_score', 
                'writing_score'
            ]

            categorical_columns =  [
                'gender', 
                'race_ethnicity', 
                'parental_level_of_education', 
                'lunch', 
                'test_preparation_course'
            ]

            num_pipeline = Pipeline(
                steps=[
                    ("inputer", SimpleImputer(strategy = "median")),
                    ("scaler", StandardScaler())
                ]
            )

            categorical_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("standrad_scaling", StandardScaler(with_mean=False))
                ]
            )

            logging.info("Numerical colums standard scaling completed")
            
            logging.info("Categoriical colums encoded completed")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", categorical_pipeline, categorical_columns)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
    def initiate_data_transformation(self, train_path, test_path):
        
        '''
        This funciton is responsible for utilizing get_data_transformer_object on train and test datasets
        
        '''
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("read train and test data completed")

            preprocessing_obj = self.get_data_transformer_object()


            logging.info("seperating input and target features completed")
            target_column_name = "math_score"           
   
            input_feature_train_df = train_df.drop(columns= [target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns= [target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"Preprocessing train and test sets")

            input_feature_train_arr = preprocessing_obj.fit_transform( input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform( input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saving preprocessing object")


            save_object(

                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)