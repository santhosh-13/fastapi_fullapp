from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # JWT settings
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    # Database settings
    database_hostname: str
    database_port: int
    database_username: str
    database_password: str
    database_name: str

    class Config:
        env_file = ".env"

settings = Settings()
