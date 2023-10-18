from sqlalchemy.engine.url import URL
from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table

from Configs.config import make_config

config = make_config()


url_object = URL.create(
    config.db.drivername,
    username=config.db.user,
    password=config.db.password,
    host=config.db.host,
    port=config.db.port,
    database=config.db.database_name, 
)


engine  = create_engine(url_object)

metadata = MetaData()

products = Table(
    'products', metadata, autoload_with=engine
)

types = Table(
    'type', metadata, autoload_with=engine
)

orders = Table(
    'orders', metadata, autoload_with=engine
)

order_list = Table(
    'order_list', metadata, autoload_with=engine
)

