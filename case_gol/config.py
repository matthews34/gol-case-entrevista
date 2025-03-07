import os


class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    ANAC_DATA_URL = os.environ["ANAC_DATA_URL"]


class DevConfig(Config):
    pass


class ProdConfig(Config):
    DATABASE = os.environ.get("DATABASE_PATH")


config_manager = {
    "dev": DevConfig,
    "prod": ProdConfig,
}
