import os
import sys
import numpy as np
import pandas as pd
import dill

from exception import CustomException
from logger import logging


def save_models(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        with open( file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
        logging.info(f" Saved model at {file_path}")
    except Exception as e:
        raise CustomException(e,sys)
