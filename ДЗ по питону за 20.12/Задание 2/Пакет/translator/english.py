def translate(text):
    words = {
        "Привет": "Hello",
        "мир": "world",
        "пока": "bye",
        "спасибо": "thank you"
    }
    result = text
    for ru, en in words.items():
        result = result.replace(ru, en)
    return result