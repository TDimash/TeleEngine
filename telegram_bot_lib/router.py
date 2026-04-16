from typing import Any, Callable, List, Optional, Union
from .types import Update
from .filters.builtin import BaseFilter

class Handler:
    def __init__(self, callback: Callable, filters: List[BaseFilter]):
        self.callback = callback
        self.filters = filters

    async def check(self, update: Update) -> bool:
        for f in self.filters:
            if not await f(update):
                return False
        return True

class Router:
    def __init__(self):
        self.message_handlers: List[Handler] = []
        self.callback_query_handlers: List[Handler] = []

    def message(self, *filters: BaseFilter):
        def decorator(callback: Callable):
            self.message_handlers.append(Handler(callback, list(filters)))
            return callback
        return decorator

    def callback_query(self, *filters: BaseFilter):
        def decorator(callback: Callable):
            self.callback_query_handlers.append(Handler(callback, list(filters)))
            return callback
        return decorator

    def include_router(self, other: 'Router'):
        self.message_handlers.extend(other.message_handlers)
        self.callback_query_handlers.extend(other.callback_query_handlers)
