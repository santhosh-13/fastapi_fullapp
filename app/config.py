from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname:str
    database_password:str
    database_port:str
    database_name:str
    database_username:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    database_path:str

    class Config:
        env_file=".env"


settings=Settings()