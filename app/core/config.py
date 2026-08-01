from pydantic import PostgresDsn, RedisDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str
    
    DATABASE_URL: PostgresDsn
    SQL_ECHO: bool = False
    
    REDIS_URL: RedisDsn
    QUEUE_REDIS_URL: RedisDsn
    
    SECRET_KEY: SecretStr
    CORS_ORIGINS: list[str]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True
    )


settings = Settings()