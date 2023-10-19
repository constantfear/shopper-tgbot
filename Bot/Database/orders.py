from sqlalchemy.sql import select
from sqlalchemy import CursorResult

from Database.connection_to_database import engine, orders, order_list, products
from Database.products import get_product_by_id

def insert_order(user_id: int, order: dict, phone: str, addres: str) -> None:
    
    with engine.connect() as conn:
        query = (
            orders.insert().values(
                user_id=user_id, 
                addres=addres, 
                phone=phone, 
                order_status = 1
            ).returning(orders.c.order_id)
        )
        order_id = conn.execute(query).first()[0]
        
        for product_id in order.keys():
            price = get_product_by_id(product_id).first()[3]
            query = (
                order_list.insert().values(
                    order_id=order_id, 
                    product_id=product_id, 
                    amount=order[product_id], 
                    total_price=price*order[product_id]
                )
            )
            conn.execute(query)
        conn.commit()

def get_orders() -> CursorResult:
    with engine.connect() as conn:
        query = (
            orders.select()
        )
        res = conn.execute(query)
        return res
    
def get_order_list(order_id: int) -> CursorResult:
    with engine.connect() as conn:
        query = (
            select(products.c.name, order_list.c.amount, order_list.c.total_price).join(products, products.c.product_id==order_list.c.product_id).where(order_list.c.order_id == order_id)
        )
        res = conn.execute(query)
        return res


def change_status(order_id: int) -> None:
    query = (
        orders.update().where(orders.c.order_id == order_id).values(order_status=2)
    )
    with engine.connect() as conn:
        conn.execute(query)
        conn.commit()