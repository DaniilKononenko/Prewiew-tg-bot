import asyncio
import logging
from aiogram import Dispatcher, Bot

from config import config
from routers import routers

async def main():
    logger = logging.getLogger(__name__)

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    bot: Bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(routers)
    
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())