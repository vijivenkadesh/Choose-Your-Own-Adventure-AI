from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import field_validator, ConfigDict



class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    ALLOWED_ORIGINS: str = ""
    OPENAI_API_KEY: str = ""
    DATABASE_URL: str = "sqlite:///./database.db"

    
    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []
    

    class Config():
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sentive = True


settings = Settings()