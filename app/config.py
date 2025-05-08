from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
settings = Settings()    