import os, sys
import logging

logging_str= f"[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

log_dir= 'logs'
os.makedirs(log_dir, exist_ok=True)

log_filepath= os.path.join(log_dir, 'running_logs.log')


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        # logging.StreamHandler(sys.stdout),
    ]
)

logger= logging.getLogger(name='DeepClassifierLogger')