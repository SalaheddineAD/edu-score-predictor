import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# creates a directory at logs_path, exist_ok=True is used so that no error is raised if the folder is already there
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig( 
    filename=LOG_FILE_PATH, 
    level=logging.INFO, 
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s'
    
    )

# just  to test logger.py
if __name__ == "__main__":
    logging.info("Logging has started")