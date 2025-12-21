def translate(text):
    words = {
        "Привет": "Bonjour",
        "мир": "monde",
        "пока": "au revoir"
    }
    result = text
    for ru, fr in words.items():
        result = result.replace(ru, fr)
    return result