#2 Поиск максимального элемента
#Создайте список из 10 чисел. Найдите и выведите максимальный элемент. Если
#список пуст, обработайте соответствующее исключение.

numbers = [45, 12, 89, 3, 67, 34, 99, 21, 5, 78]

try:
    if not numbers:
        raise ValueError("Список пуст")
    max_element = max(numbers)
    print(f"Максимальный элемент: {max_element}")
except ValueError as e:
    print(e)