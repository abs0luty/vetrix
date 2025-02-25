from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_DATABASE_URL: str
    MONGO_DATABASE_NAME: str

    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str
    PASSWORD_SALT: str

    CLIENT_ORIGIN: str

    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str
    EMAIL_FROM: EmailStr

    class Config:
        env_file = './.env'


settings = Settings()
