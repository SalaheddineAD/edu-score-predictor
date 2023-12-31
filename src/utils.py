import os
import sys
import numpy as np
import pandas as pd
import dill

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


from exception import CustomException
from logger import logging


def save_object(file_path, obj): 
    try:
        dir_path = os.path.dirname(file_path)

        with open( file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
        logging.info(f" Saved model at {file_path}")
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_model(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            model_params =param[list(models.keys())[i]]
            # model_params = list(param.values())[i]

            gs = GridSearchCV(model, model_params, cv=5)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]]= test_score

        return report

    except Exception as e:
        raise CustomException(e,sys)
    

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        return obj
    except Exception as e:
        raise CustomException(e,sys)