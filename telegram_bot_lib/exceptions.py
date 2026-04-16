class TelegramBotError(Exception):
    """Base exception for the library."""
    pass

class TelegramAPIError(TelegramBotError):
    def __init__(self, message: str, error_code: Optional[int] = None):
        super().__init__(message)
        self.error_code = error_code

class NetworkError(TelegramBotError):
    pass

class ValidationError(TelegramBotError):
    pass

class SkipHandler(Exception):
    """Raised to skip the current handler and continue to the next one."""
    pass
