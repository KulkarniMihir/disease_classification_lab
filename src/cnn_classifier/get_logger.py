import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#create directory to store logs
log_dir = "logs"
log_filepath = os.path.join(log_dir, "runnning_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO, #fetch information
    format=logging_str, #initialize information in format

    handlers=[
        logging.FileHandler(log_filepath),  #create files
        logging.StreamHandler(sys.stdout)   #print logs on terminal
    ]
)

#logging name
logger = logging.getLogger("cnn_classifier_logger")