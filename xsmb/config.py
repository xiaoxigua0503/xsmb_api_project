"""Cấu hình chung: API endpoint, API key và logging."""
import os
from dotenv import load_dotenv
import logging

load_dotenv()

api_url = "https://xosoapi.online/api/v1/vietnam/draws"
api_key = os.getenv("api_key")
REGION_CODE = "MB"

def setup_logging(level: str = "INFO") -> None:
    logging.basicConfig(
        level=level.upper(),
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )
