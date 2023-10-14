from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    admin_id: int
    seller_id: int

@dataclass
class DataBase:
    host: str
    database_name: str
    user: str
    password: str

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
            host = env('HOST'),
            database_name = env('DB_NAME'),
            user = env('USER'),
            password = env('PASSWORD')
        )
    )