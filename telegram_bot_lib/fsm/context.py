from typing import Any, Dict, Optional
from .storage import MemoryStorage

class FSMContext:
    def __init__(self, storage: MemoryStorage, chat_id: int, user_id: int):
        self.storage = storage
        self.chat_id = chat_id
        self.user_id = user_id

    async def set_state(self, state: Optional[str]):
        await self.storage.set_state(self.chat_id, self.user_id, state)

    async def get_state(self) -> Optional[str]:
        return await self.storage.get_state(self.chat_id, self.user_id)

    async def set_data(self, data: Dict[str, Any]):
        await self.storage.set_data(self.chat_id, self.user_id, data)

    async def get_data(self) -> Dict[str, Any]:
        return await self.storage.get_data(self.chat_id, self.user_id)

    async def clear(self):
        await self.storage.set_state(self.chat_id, self.user_id, None)
        await self.storage.set_data(self.chat_id, self.user_id, {})
