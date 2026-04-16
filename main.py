import asyncio
import logging
from teleengine.bot import Bot
from teleengine.dispatcher import Dispatcher
from teleengine.types import Message, CallbackQuery
from teleengine.filters.builtin import CommandFilter, TextFilter
from teleengine.keyboards import InlineKeyboardBuilder, InlineKeyboardButton

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher(bot)

@dp.message(CommandFilter(["start"]))
async def cmd_start(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Help", callback_data="help"))
    builder.add(InlineKeyboardButton(text="About", callback_data="about"))
    
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Hello, {message.from_user.first_name}! I'm an async bot.",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(TextFilter("help"))
async def cb_help(callback: CallbackQuery, bot: Bot):
    await bot.send_message(
        chat_id=callback.message.chat.id,
        text="This is a help message."
    )

async def main():
    try:
        await dp.start_polling()
    finally:
        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
