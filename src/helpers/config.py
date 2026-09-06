from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    
    APP_NAME:str 
    APP_VERSION:str 
    OPENAI_API_KEY :str 
    
    
    class Config:
        env_file=".env" # all things inside .env file will be a class 


def get_settings(): # returns object from class(settings)
    return Settings()      