import logging
import os
import sys
import time
from logging.handlers import RotatingFileHandler


def setup_logger():
    logger = logging.getLogger(__name__)

    logger.setLevel(logging.INFO)

    # Create a console handler and set the level to INFO
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.isatty = lambda: False  # Disable ANSI color codes

    # Determine the log file path
    log_file_path = os.environ.get('LOG_FILE_PATH')
    current_time = time.strftime("%Y%m%d_%H%M%S")
    log_file_name = f'my_log_{current_time}.log'

    if log_file_path is None:
        log_file_path = os.path.join(os.getcwd(), log_file_name)
    else:
        log_file_path = os.path.join(log_file_path, log_file_name)

    # Create a file handler and set the level to INFO
    file_handler = RotatingFileHandler(log_file_path, maxBytes=1024 * 1024, backupCount=5)
    file_handler.setLevel(logging.INFO)

    # Create a formatter for file logs
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # Create a formatter for console logs (without date and time)
    console_formatter = logging.Formatter('%(message)s')
    console_handler.setFormatter(console_formatter)

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


global_logger = setup_logger()
