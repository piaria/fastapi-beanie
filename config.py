from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb://admin:admin@localhost:27017"
    SERVICE_DB: str = "my_todo"


settings = Settings()
