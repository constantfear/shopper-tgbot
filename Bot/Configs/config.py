from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    admin_id: int
    seller_id: int

@dataclass
class DataBase:
    drivername: str
    host: str
    port: str
    user: str
    password: str
    database_name: str

@dataclass
class Config:
    tg_bot: TgBot
    db: DataBase

def make_config(env_path: str or None = None) -> Config:
    env = Env()
    env.read_env(env_path)
    return Config(
        tg_bot=TgBot(
            token = env('BOT_TOKEN'),
            admin_id = int(env('ADMIN_ID')),
            seller_id = int(env('SELLER_ID')),
        ),
        db=DataBase(
            drivername = env('DRIVER_NAME'),
            host = env('HOST'),
            port = env('PORT'),
            user = env('DB_USERNAME'),
            password = env('PASSWORD'),
            database_name = env('DB_NAME')
        )
    )