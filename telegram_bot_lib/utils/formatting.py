import html

def escape_html(text: str) -> str:
    return html.escape(text)

def bold(text: str) -> str:
    return f"<b>{text}</b>"

def italic(text: str) -> str:
    return f"<i>{text}</i>"

def code(text: str) -> str:
    return f"<code>{text}</code>"
