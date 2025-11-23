from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    database_path: str

    class Config:
        env_file=".env"

settings = Settings()
  