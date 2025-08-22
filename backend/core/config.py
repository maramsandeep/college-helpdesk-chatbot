# backend/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "College Helpdesk Chatbot"
    debug: bool = True
    mongo_uri: str = "mongodb://localhost:27017"

    # This tells Pydantic to allow extra env vars from your .env file
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8"
    )

# Instantiate once for the app to use
settings = Settings()
