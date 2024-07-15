import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#create log file inside the log directory
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


#initializing the logging system
logging.basicConfig(
    level= logging.INFO, #logging information
    format= logging_str, #logging format

    handlers=[
        logging.FileHandler(log_filepath), #print the logging in the terminal as well
        logging.StreamHandler(sys.stdout) #I can see my log in both terminal and log file
          ]
    )



        
    

logger = logging.getLogger("cnnClassifierLogger")