from pydantic_settings import BaseSettings
from decouple import config
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    PROJECT_NAME:str = "Monika Verein API"
    PROJECT_VERSION: str = "1.0.0"

    DB_USER : str = config("DB_USER")
    DB_PASSWORD : str = config("DB_PASSWORD")
    DB_HOST : str = config("DB_HOST","localhost")
    DB_PORT : str = config("DB_PORT", 5432)
    DB_NAME : str = config("DB_NAME")
    DB_TYPE : str = config("DB_TYPE", "sqlite")
    DATABASE_URL : str = f"DBql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    STRIPE_SECRET_KEY : str = config("STRIPE_SECRET_KEY")
    STRIPE_PUBLISHABLE_KEY : str =config("STRIPE_PUBLISHABLE_KEY")
    STRIPE_SUCCESS_URL : str = config("STRIPE_SUCCESS_URL")
    STRIPE_CANCEL_URL : str = config("STRIPE_CANCEL_URL")

    TEST_MODE_ACTIVE : bool = config("TEST_MODE_ACTIVE")

settings = Settings()