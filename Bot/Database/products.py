from sqlalchemy.sql import select, insert
from sqlalchemy import Engine, MetaData, Table, CursorResult

from Configs.config import make_config



def get_products(engine: Engine, type: int) -> CursorResult:

    metadata = MetaData()
    products = Table(
        'products', metadata, autoload_with=engine
    )
    types = Table(
        'type', metadata, autoload_with=engine
    )

    products_cols = products.c
    type_cols = types.c

    with engine.connect() as conn:
        query = (
            select(products, type_cols.type_name).join(types, products_cols.product_type==type_cols.type_id).where(products.c.product_type==type)
        )
        res = conn.execute(query)
        return res
    
def get_types(engine: Engine) -> CursorResult:

    metadata = MetaData()
    type = Table(
        'type', metadata, autoload_with=engine
    )

    with engine.connect() as conn:
        query = (
            select(type.c.type_id, type.c.type_name)
        )
        res = conn.execute(query)
        return res

def add_products(engine: Engine, name:str, description:str, price: int, product_type: int) -> None:
    
    metadata = MetaData()
    products = Table(
        'products', metadata, autoload_with=engine
    )

    with engine.connect() as conn:
        query = (
            products.insert().values(
                name = name, description = description, price = price, product_type = product_type
            )
        )
        conn.execute(query)
        conn.commit()

