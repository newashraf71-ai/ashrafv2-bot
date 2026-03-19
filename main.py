import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os
import random

API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.reply("🚀 Welcome Ashraf! \n\n/ashraf - Special message\n/panna - Get prediction\n/help - Help")

@dp.message(Command('ashraf'))
async def ashraf_command(message: types.Message):
    await message.reply("✨ **Ashraf Special** ✨\n\n🔥 Panna Poren!\n🚀 100% Correct")

@dp.message(Command('panna'))
async def panna_command(message: types.Message):
    predictions = [
        "✅ Today is your day - Panna Poren! 🚀",
        "🎯 Green Signal - 100% Win! 💚",
        "💰 Jackpot today! ⚡",
        "🔮 Go for it - Super Result! 💫",
        "🔥 Definitely Win - Ashraf Style! 👑"
    ]
    await message.reply(f"🔮 **Ashraf Prediction** 🔮\n\n{random.choice(predictions)}\n\n💫 _Try it..._")

@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.reply("📚 **Help** 📚\n\n/start - Start the bot\n/ashraf - Special message\n/panna - Get prediction\n/help - This help")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
