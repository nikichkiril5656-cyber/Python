import importlib

def translate(text, lang):
    try:
        module = importlib.import_module(f"translator.{lang}")
        return module.translate(text)
    except ModuleNotFoundError:
        return "Язык не найден"