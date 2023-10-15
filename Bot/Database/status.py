from sqlalchemy.sql import select
from sqlalchemy import Engine, MetaData, Table, CursorResult

from Configs.config import make_config



def get_status(engine: Engine) -> CursorResult:

    metadata = MetaData()
    cookies = Table(
        'status', metadata, autoload_with=engine
    )

    cols = cookies.c

    with engine.connect() as conn:
        query = (
            select(cols.status_id, cols.status_name)
        )
        res = conn.execute(query)
        return res

