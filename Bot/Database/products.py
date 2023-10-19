from sqlalchemy.sql import select
from sqlalchemy import CursorResult

from Database.connection_to_database import engine, products, types



def get_products_by_type(type: int) -> CursorResult:

    products_cols = products.c
    type_cols = types.c

    with engine.connect() as conn:
        query = (
            select(products_cols.product_id, products_cols.name, products_cols.description, products_cols.price, type_cols.type_name).join(types, products_cols.product_type==type_cols.type_id).where(products.c.product_type==type)
        )
        res = conn.execute(query)
        return res
    
def get_types() -> CursorResult:

    with engine.connect() as conn:
        query = (
            select(types.c.type_id, types.c.type_name)
        )
        res = conn.execute(query)
        return res

def add_products(name:str, description:str, price: int, product_type: int) -> None:

    with engine.connect() as conn:
        query = (
            products.insert().values(
                name = name, description = description, price = price, product_type = product_type
            )
        )
        conn.execute(query)
        conn.commit()

def get_product_by_id(id: int) -> CursorResult:

    products_cols = products.c
    type_cols = types.c


    with engine.connect() as conn:
        query = (
            select(products_cols.product_id, products_cols.name, products_cols.description, products_cols.price, type_cols.type_name).join(types, products_cols.product_type==type_cols.type_id).where(products.c.product_id==id)
        )
        res = conn.execute(query)
        return res
    
def update_product_name(id: int,  name: str) -> None:

    query = (
        products.update().where(products.c.product_id == id).values(name=name)
    )
    with engine.connect() as conn:
        conn.execute(query)
        conn.commit()

def update_product_description(id: int,  description: str) -> None:

    query = (
        products.update().where(products.c.product_id == id).values(description=description)
    )
    with engine.connect() as conn:
        conn.execute(query)
        conn.commit()

def update_product_price(id: int,  price: int) -> None:

    query = (
        products.update().where(products.c.product_id == id).values(price=price)
    )

    with engine.connect() as conn:
        conn.execute(query)
        conn.commit()

def delete_product(id: int) -> None:

    query = (
        products.delete().where(products.c.product_id == id)
    )

    with engine.connect() as conn:
        conn.execute(query)
        conn.commit()
        