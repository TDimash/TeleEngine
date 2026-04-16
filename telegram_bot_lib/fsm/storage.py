from typing import Any, Dict, Optional

class State:
    def __init__(self, name: str):
        self.name = name

class StateGroup:
    pass

class MemoryStorage:
    def __init__(self):
        self.states: Dict[str, str] = {}
        self.data: Dict[str, Dict[str, Any]] = {}

    def _get_key(self, chat_id: int, user_id: int) -> str:
        return f"{chat_id}:{user_id}"

    async def set_state(self, chat_id: int, user_id: int, state: Optional[str]):
        key = self._get_key(chat_id, user_id)
        if state is None:
            self.states.pop(key, None)
        else:
            self.states[key] = state

    async def get_state(self, chat_id: int, user_id: int) -> Optional[str]:
        return self.states.get(self._get_key(chat_id, user_id))

    async def set_data(self, chat_id: int, user_id: int, data: Dict[str, Any]):
        self.data[self._get_key(chat_id, user_id)] = data

    async def get_data(self, chat_id: int, user_id: int) -> Dict[str, Any]:
        return self.data.get(self._get_key(chat_id, user_id), {})
