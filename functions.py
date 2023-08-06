from transliterate import to_cyrillic, to_latin

async def editText(msg: str) -> str:
    if msg.isascii():
        msg = to_cyrillic(msg)
    else:
        msg = to_latin(msg)
    return msg