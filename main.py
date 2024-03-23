from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from asyncio import run
import funksiyalar
import states

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(5165396993, "Bot ishga tushdi! ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(5165396993, "Bot ishdan to'xtadi! ❗")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    dp.message.register(funksiyalar.start_command_answer, CommandStart())
    dp.message.register(funksiyalar.get_user_realy_name_answer, states.get_user_realy_name.name)
    dp.message.register(funksiyalar.get_ref_link_answer, F.text == "Referal havola")
    dp.message.register(funksiyalar.get_user_ball_answer, F.text == "Mening ballarim")

    bot = Bot("6923568104:AAG5CQOmPU0_cG-Ym3dwdGNC5ZFjRcYB9cY")
    await dp.start_polling(bot, polling_timeout=1)

run(start())