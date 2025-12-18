import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


script_dir = os.path.dirname(os.path.abspath(__file__))  # папка скрипта
file_path = os.path.join(script_dir, "text.txt")         # путь к файлу


bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart()) # команда старт
async def start_cmd(message: types.Message):
    with open(file_path, "r", encoding="utf-8") as f:
        await message.answer(f.read())


async def on_startup():
    print('бот запущен')


async def on_shutdown():
    print('бот лег')


async def main(): # функция запуска бота
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())



    