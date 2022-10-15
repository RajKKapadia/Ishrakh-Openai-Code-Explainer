import sys
import logging

format = '[%(asctime)s: %(levelname)s: %(module)s]: %(message)s'

logging.basicConfig(
    level=logging.INFO, 
    format=format,
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)