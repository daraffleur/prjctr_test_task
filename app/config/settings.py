from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    SERVER_NAME: str = "API"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    ENV: str = "production"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive: bool = True


settings: Settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
