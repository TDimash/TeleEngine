from typing import List, Optional, Union
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None

class Chat(BaseModel):
    id: int
    type: str
    title: Optional[str] = None
    username: Optional[str] = None

class Message(BaseModel):
    message_id: int
    from_user: Optional[User] = Field(None, alias="from")
    date: int
    chat: Chat
    text: Optional[str] = None
    reply_markup: Optional[Any] = None

class PhotoSize(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: Optional[int] = None

class Document(BaseModel):
    file_id: str
    file_unique_id: str
    thumbnail: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None

class CallbackQuery(BaseModel):
    id: str
    from_user: User = Field(..., alias="from")
    message: Optional[Message] = None
    data: Optional[str] = None

class Update(BaseModel):
    update_id: int
    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    callback_query: Optional[CallbackQuery] = None

# Add more models as needed...
