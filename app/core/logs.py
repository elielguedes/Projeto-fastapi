import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok = True)
def setup_loguin():
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s",)

    file_handler = RotatingFileHandler(f"{LOG_DIR}/app.log", maxBytes = 5_000_000 , backupCount = 3)

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logging.basicConfig(level = logging.INFO , handlers= [file_handler, console_handler])

