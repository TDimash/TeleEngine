from typing import Any, Callable, Dict, Awaitable

class BaseMiddleware:
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any]
    ) -> Any:
        return await handler(event, data)
