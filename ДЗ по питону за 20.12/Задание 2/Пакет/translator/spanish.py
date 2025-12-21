def translate(text):
    words = {
        "Привет": "Hola",
        "мир": "mundo",
        "пока": "adiós"
    }
    result = text
    for ru, es in words.items():
        result = result.replace(ru, es)
    return result