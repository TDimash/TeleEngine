from typing import Any, Callable, List, Optional
from .types import Update

class BaseFilter:
    async def __call__(self, update: Update) -> bool:
        raise NotImplementedError

class CommandFilter(BaseFilter):
    def __init__(self, commands: List[str], prefix: str = "/"):
        self.commands = commands
        self.prefix = prefix

    async def __call__(self, update: Update) -> bool:
        if not update.message or not update.message.text:
            return False
        text = update.message.text
        if not text.startswith(self.prefix):
            return False
        command = text[len(self.prefix):].split()[0]
        return command in self.commands

class TextFilter(BaseFilter):
    def __init__(self, text: str, exact: bool = True):
        self.text = text
        self.exact = exact

    async def __call__(self, update: Update) -> bool:
        if not update.message or not update.message.text:
            return False
        if self.exact:
            return update.message.text == self.text
        return self.text in update.message.text
