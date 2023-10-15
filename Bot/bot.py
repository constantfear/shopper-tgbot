from aiogram import Bot, Dispatcher
from Configs.config import make_config
from aiogram.fsm.storage.memory import MemoryStorage

from Handlers import comand_handlers, make_order_handlers, seller_connection_handlers, other_handlers, show_products, admin_handlers, add_product_handlers

import asyncio
import logging

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Starting bot')
    
    config = make_config(env_path='.env')

    storage = MemoryStorage()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(storage=storage)

    dp.include_router(comand_handlers.router)
    dp.include_router(admin_handlers.router)
    dp.include_router(add_product_handlers.router)
    dp.include_router(show_products.router)
    dp.include_router(make_order_handlers.router)
    dp.include_router(seller_connection_handlers.router)
    dp.include_router(other_handlers.router)
    
    await bot.delete_webhook(drop_pending_updates=True) #drop in prod
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')