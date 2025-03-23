from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PG_USERNAME: str
    PG_PASSWORD: str
    PG_DATABASE: str
    PG_HOST: str
    PG_PORT: int

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
