import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
await message.answer(
"🌟 Welcome to Digital Marketing Hub! 🌟\n\n"
"Welcome! यहाँ आप हमारे digital products और subscriptions "
"के बारे में जानकारी प्राप्त कर सकते हैं।\n\n"
"🛍️ Products देखने के लिए /products लिखें\n"
"💬 Support के लिए /support लिखें"
)

@dp.message(Command("products"))
async def products_handler(message: Message):
await message.answer(
"🛍️ Digital Marketing Hub Products\n\n"
"हमारी product list जल्द उपलब्ध होगी।\n"
"अभी product और pricing की जानकारी के लिए support से संपर्क करें।"
)

@dp.message(Command("support"))
async def support_handler(message: Message):
await message.answer(
"💬 Customer Support\n\n"
"कृपया अपने सवाल और Order ID के साथ support team से संपर्क करें।"
)

async def main():
if not TOKEN:
raise RuntimeError("BOT_TOKEN environment variable is missing")

bot = Bot(token=TOKEN)
try:
    await dp.start_polling(bot)
finally:
    await bot.session.close()

if name == "main":
asyncio.run(main())
