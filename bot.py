import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from db import init_db, save_lead

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


class Form(StatesGroup):
      name = State()
      phone = State()
      email = State()


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
      await state.set_state(Form.name)
      await message.answer("Привет! Как вас зовут?")


@dp.message(Form.name)
async def get_name(message: Message, state: FSMContext):
      await state.update_data(name=message.text)
      await state.set_state(Form.phone)
      kb = ReplyKeyboardMarkup(
          keyboard=[[KeyboardButton(text="Поделиться номером", request_contact=True)]],
          resize_keyboard=True,
      )
      await message.answer("Оставьте номер телефона:", reply_markup=kb)


@dp.message(Form.phone, F.contact)
async def get_phone_contact(message: Message, state: FSMContext):
      await state.update_data(phone=message.contact.phone_number)
      await state.set_state(Form.email)
      await message.answer("И email для связи:")


@dp.message(Form.phone)
async def get_phone_text(message: Message, state: FSMContext):
      await state.update_data(phone=message.text)
      await state.set_state(Form.email)
      await message.answer("И email для связи:")


@dp.message(Form.email)
async def get_email(message: Message, state: FSMContext):
      data = await state.update_data(email=message.text)
      await state.clear()

    save_lead(data["name"], data["phone"], data["email"])

    await message.answer("Спасибо! Заявка принята, скоро с вами свяжутся.")

    if ADMIN_CHAT_ID:
              await bot.send_message(
                            ADMIN_CHAT_ID,
                            f"Новая заявка:\nИмя: {data['name']}\nТелефон: {data['phone']}\nEmail: {data['email']}",
              )


async def main():
      init_db()
      await dp.start_polling(bot)


if __name__ == "__main__":
      asyncio.run(main())
  
