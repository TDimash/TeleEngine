import asyncio
import logging
from typing import Any, Dict, Optional, Union
import aiohttp
from .exceptions import TelegramAPIError, NetworkError

logger = logging.getLogger(__name__)

class TelegramAPI:
    """Low-level Telegram Bot API client."""
    
    def __init__(self, token: str, session: Optional[aiohttp.ClientSession] = None):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        self._session = session
        self._own_session = False

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
            self._own_session = True
        return self._session

    async def request(self, method: str, params: Optional[Dict[str, Any]] = None, data: Optional[Any] = None) -> Dict[str, Any]:
        session = await self._get_session()
        url = f"{self.base_url}/{method}"
        
        try:
            async with session.post(url, params=params, data=data) as response:
                if response.status == 429:
                    retry_after = int(response.headers.get("Retry-After", 1))
                    logger.warning(f"Rate limited. Retrying after {retry_after} seconds.")
                    await asyncio.sleep(retry_after)
                    return await self.request(method, params, data)
                
                result = await response.json()
                if not result.get("ok"):
                    raise TelegramAPIError(result.get("description", "Unknown error"), result.get("error_code"))
                return result["result"]
        except aiohttp.ClientError as e:
            raise NetworkError(f"Network error: {e}")

    async def close(self):
        if self._own_session and self._session:
            await self._session.close()
