from typing import List
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")

API_PREFIX = "/api"
VERSION = "0.0.0"

DEBUG: bool = config("DEBUG", cast=bool, default=False)
PROJECT_NAME: str = config("PROJECT_NAME", default="eastvantage AddressBook API")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default=["*"],
)
