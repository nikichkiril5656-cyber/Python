import importlib

def calculate(a, b, operation):
    try:
        module = importlib.import_module(operation)
        return module.operate(a, b)
    except ModuleNotFoundError:
        return "Неизвестная операция"