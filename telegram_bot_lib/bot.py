import asyncio
import logging
from typing import List, Optional
from .api import TelegramAPI
from .types import Update, Message

logger = logging.getLogger(__name__)

class Bot:
    """Main Bot class."""
    
    def __init__(self, token: str):
        self.api = TelegramAPI(token)
        self.token = token

    async def send_message(self, chat_id: Union[int, str], text: str, **kwargs) -> Message:
        payload = {"chat_id": chat_id, "text": text, **kwargs}
        result = await self.api.request("sendMessage", data=payload)
        return Message(**result)

    async def edit_message_text(self, text: str, chat_id: Optional[Union[int, str]] = None, message_id: Optional[int] = None, inline_message_id: Optional[str] = None, **kwargs) -> Union[Message, bool]:
        payload = {"text": text, **kwargs}
        if chat_id: payload["chat_id"] = chat_id
        if message_id: payload["message_id"] = message_id
        if inline_message_id: payload["inline_message_id"] = inline_message_id
        result = await self.api.request("editMessageText", data=payload)
        if isinstance(result, bool): return result
        return Message(**result)

    async def delete_message(self, chat_id: Union[int, str], message_id: int) -> bool:
        payload = {"chat_id": chat_id, "message_id": message_id}
        return await self.api.request("deleteMessage", data=payload)

    async def send_photo(self, chat_id: Union[int, str], photo: Any, **kwargs) -> Message:
        payload = {"chat_id": chat_id, "photo": photo, **kwargs}
        result = await self.api.request("sendPhoto", data=payload)
        return Message(**result)

    async def answer_callback_query(self, callback_query_id: str, text: Optional[str] = None, show_alert: bool = False, **kwargs) -> bool:
        payload = {"callback_query_id": callback_query_id, "text": text, "show_alert": show_alert, **kwargs}
        return await self.api.request("answerCallbackQuery", data=payload)

    async def get_updates(self, offset: Optional[int] = None, limit: int = 100, timeout: int = 30) -> List[Update]:
        params = {"offset": offset, "limit": limit, "timeout": timeout}
        result = await self.api.request("getUpdates", params=params)
        return [Update(**u) for u in result]

    async def close(self):
        await self.api.close()
