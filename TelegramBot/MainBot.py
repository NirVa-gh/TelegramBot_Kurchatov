import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html     # Основа
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import CallbackQuery


from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton  #Импорт модулей для кнопок


TOKEN = "8053915958:AAG_pZVHkOj0YxgEjSN-4wWzsSffTI39_hU"   # Токен бота

dp = Dispatcher()

#--------------<Блок кнопок>-------------------------------


#--------------------------------------------------



@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
async def main() -> None:

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

@dp.message(Command = ("testOne"))    ## ReplyKeyboardMarkup
async def process_greet_command(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_first = KeyboardButton(text="Button_first")
    button_second = KeyboardButton(text="Button_second")
    keyboard.add(button_second,button_first)
    await message.answer("Выберите кнопку", reply_markup=keyboard)
@dp.message(Command = ("testTwo"))
async def inline_command_handler(message: Message):
    keyboard = InlineKeyboardMarkup()
    button_first = InlineKeyboardButton("Inline button_first", callback_data="button_one")
    button_second = InlineKeyboardButton("Inline button_second", callback_data="button_two")
    keyboard.add(button_first,button_second)
    await message.answer("Press to button", reply_markup=keyboard)

@dp.callback_query(lambda c:c.data in ["button_first","buttom_second"])
async def procces_callback_button(callback: CallbackQuery):
    if callback.data == "button_one":
        await callback.answer("button_one")
    elif callback.data == "button_two":
        await callback.answer("button_two")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())