from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from bot_menu import get_keyboard, get_remind_keyboard
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified
from contextlib import suppress
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import os
bot_TOKEN =os.environ.get('bot_TOKEN')
print(f'bot_token ={bot_TOKEN}')
# Объект бота
bot = Bot(token=bot_TOKEN, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    print(message.from_user)
    print(message.from_user.id)
    print(message.from_user.first_name)
    print(message.from_user.last_name)
    print(message.from_user.username)
    await message.answer("Как подавать котлеты?")


t_zones = {"+00:00": "Etc/GMT+0",
         "+01:00": "Etc/GMT-1",
         "+02:00": "Etc/GMT-2",
         "+03:00": "Etc/GMT-3",
         "+03:30": "Iran",
         "+04:00": "Etc/GMT-4",
         "+04:30": "Asia/Kabul",
         "+05:00": "Etc/GMT-5",
         "+05:30": "Asia/Colombo",
         "+05:45": "Asia/Katmandu",
         "+06:00": "Etc/GMT-6",
         "+06:30": "Asia/Yangon",
         "+07:00": "Etc/GMT-7",
         "+08:00": "Etc/GMT-8",
         "+08:45": "Australia/Eucla",
         "+09:00": "Etc/GMT-9",
         "+09:30": "Australia/Darwin",
         "+10:00": "Etc/GMT-10",
         "+10:30": "Australia/Adelaide",
         "+11:00": "Etc/GMT-11",
         "+12:00": "Etc/GMT-12",
         "+13:00": "Etc/GMT-13",
         "+13:45": "Pacific/Chatham",
         "+14:00": "Etc/GMT-14",
         "-01:00": "Etc/GMT+1",
         "-02:00": "Etc/GMT+2",
         "-02:30": "Canada/Newfoundland",
         "-03:00": "Etc/GMT+3",
         "-04:00": "Etc/GMT+4",
         "-05:00": "Etc/GMT+5",
         "-06:00": "Etc/GMT+6",
         "-07:00": "Etc/GMT+7",
         "-08:00": "Etc/GMT+8",
         "-09:00": "Etc/GMT+9",
         "-09:30": "Pacific/Marquesas",
         "-10:00": "Etc/GMT+10",
         "-11:00": "Etc/GMT+11",
         "-12:00": "Etc/GMT+12"}

tz_k = t_zones.keys()

@dp.message_handler(commands="set_timezone")
async def set_timezone(message: types.Message):
    await message.answer(f'По умолчанию установлен часовой пояс "<b>UTC+03:00</b>"')
    await message.answer(f'🌍 Укажите разницу во времени относительно UTC', reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="tz_"))
async def callbacks_timezone(call: types.CallbackQuery):
    action = call.data.split("_")[1]
    if action in tz_k:
        print(f'{action=}')
        await call.message.delete_reply_markup()
        print(call.from_user)
        await call.message.answer(f'Установлен часовой пояс "<b>UTC{action}</b>".\nТеперь можно вводить напоминания!\nДля получения дополнительной информации введите команду /help.')
    await call.answer()




@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

if __name__ == "__main__":
    # Запуск бота
    print("Bot is running ....")
    executor.start_polling(dp, skip_updates=False)
    print("Bot stoped.")
