from typing import Callable

from fastapi import FastAPI
from logging.config import dictConfig
from app.api.logging.config import LogConfig


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        dictConfig(LogConfig().dict())
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        pass
    return stop_app
