from apscheduler.schedulers.asyncio import AsyncIOScheduler

import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main
from app.database.requests import get_inactive_users

import app.localization as local
import app.keyboards as kb

async def send_daily_reminder(bot: Bot):
    inactive_users = await get_inactive_users() # получаем список пользователей, не выполнявших задания сегодня
    for user in inactive_users:
        if user.is_reminder_enabled == 1:
            daily_reminder_message = await local.get_text(user.language, "daily_reminder")
            disable_reminder_keyboard = await kb.create_inline_keyboard(kb.TURN_OFF_REMINDER_SCHEME, user.language)
            await bot.send_message(user.tg_id, daily_reminder_message, reply_markup=disable_reminder_keyboard)

def setup_scheduler(bot: Bot):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_daily_reminder, "cron", hour=18, args=[bot])  # планируем выполнение функции каждый день в 18:00
    scheduler.start()

async def main():
    await async_main()
    bot = Bot(token='') # подключаемся к боту
    dp = Dispatcher() # создаём обработчик
    dp.include_router(router) # чтобы dp был routerом в других файлах
    setup_scheduler(bot)
    await dp.start_polling(bot) # постоянно обращается к серверу ТГ и спрашивает, не пришло ли что-то в бот

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt: # CTRL+C - выключить бот
        print("The bot is disabled.")