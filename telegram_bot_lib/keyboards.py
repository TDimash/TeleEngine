from typing import List, Optional
from pydantic import BaseModel

class InlineKeyboardButton(BaseModel):
    text: str
    callback_data: Optional[str] = None
    url: Optional[str] = None

class InlineKeyboardMarkup(BaseModel):
    inline_keyboard: List[List[InlineKeyboardButton]]

class InlineKeyboardBuilder:
    def __init__(self):
        self.buttons: List[List[InlineKeyboardButton]] = []

    def add(self, *buttons: InlineKeyboardButton):
        if not self.buttons:
            self.buttons.append([])
        self.buttons[-1].extend(buttons)
        return self

    def row(self, *buttons: InlineKeyboardButton):
        self.buttons.append(list(buttons))
        return self

    def as_markup(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=self.buttons)
