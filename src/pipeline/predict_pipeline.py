import sys
import pandas as pd
from exception import CustomException
from src.utils import load_object



class PredictPipeline:
    '''
    
    responsible to prediction
    
    '''
    def __init__(self):
        pass
    
    def predict(self, features):
        '''
        predict gets the non-processed input as a dataframe then preprocess it then predicts. 
        It uses the preprocessor.pkl and model.pll
        
        '''
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'

            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)

            print("After Loading")
            data_preprocessed = preprocessor.transform(features)
            print(data_preprocessed)
            print("transformation working")
            predictions = model.predict(data_preprocessed)
            print("model working")
            
            return predictions
        
        except Exception as e:
            raise CustomException(e,sys)





class CustomData:
    '''
    CUstomdata is used to transform the input data of the form into a dataframe

    '''
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
        
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.reading_score = reading_score
        self.writing_score = writing_score
        self.lunch= lunch
        self.test_preparation_course = test_preparation_course

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender" : [self.gender],
                "race_ethnicity" : [self.race_ethnicity],
                "parental_level_of_education" : [self.parental_level_of_education],
                "lunch" : [self.lunch],
                "test_preparation_course" : [self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score" : [self.writing_score]
            }

            data = pd.DataFrame(custom_data_input_dict)
            return data
        
        except Exception as e:
            raise CustomException(e,sys)


