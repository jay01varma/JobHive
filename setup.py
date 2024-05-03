import os
import datetime as dt
import logging
from pathlib import Path

# Define directory names as constants
JOB_DB_DIR = "job_db"
LOGS_DIR = "logs"

def create_db_dir() -> None:
    """
    Creates database directory for scraped jobs.
    """
    try:
        os.makedirs(JOB_DB_DIR, exist_ok=True)
        logging.info("Job database directory created successfully.")
    except Exception as e:
        logging.error(f"Failed to create job database directory: {e}")
        raise  # Raise an exception to indicate failure

def create_log_dir() -> None:
    """
    Sets up logging file for the scraper.
    """
    try:
        os.makedirs(LOGS_DIR, exist_ok=True)
        logging.info("Logs directory created successfully.")
        LOGGING_DIR = f'{LOGS_DIR}/job-scraping-{dt.datetime.today().strftime("%Y%m%d")}.log'
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)-8s %(message)s",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(Path(LOGGING_DIR)),
            ],
        )
    except Exception as e:
        logging.error(f"Failed to create logs directory: {e}")
        raise  # Raise an exception to indicate failure
