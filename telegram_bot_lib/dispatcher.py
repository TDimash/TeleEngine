import asyncio
import logging
from typing import List, Optional
from .bot import Bot
from .router import Router
from .types import Update
from .fsm.storage import MemoryStorage

logger = logging.getLogger(__name__)

class Dispatcher(Router):
    def __init__(self, bot: Bot, storage: Optional[Any] = None):
        super().__init__()
        self.bot = bot
        self.storage = storage or MemoryStorage()
        self._running = False

    async def feed_update(self, update: Update):
        if update.message:
            for handler in self.message_handlers:
                if await handler.check(update):
                    await handler.callback(update.message, bot=self.bot)
                    return
        elif update.callback_query:
            for handler in self.callback_query_handlers:
                if await handler.check(update):
                    await handler.callback(update.callback_query, bot=self.bot)
                    return

    async def start_polling(self):
        self._running = True
        offset = None
        logger.info("Starting polling...")
        while self._running:
            try:
                updates = await self.bot.get_updates(offset=offset)
                for update in updates:
                    offset = update.update_id + 1
                    asyncio.create_task(self.feed_update(update))
            except Exception as e:
                logger.error(f"Error in polling: {e}")
                await asyncio.sleep(5)

    def stop(self):
        self._running = False
