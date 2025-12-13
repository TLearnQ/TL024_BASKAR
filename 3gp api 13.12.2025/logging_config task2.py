import logging
import json


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    
    