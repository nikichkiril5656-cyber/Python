import random


def make_password(length=8, special_chars=True, big_letters=True, numbers=True):
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    all_chars = small_letters

    if big_letters:
        all_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if numbers:
        all_chars += "0123456789"

    if special_chars:
        all_chars += "!@#$%^&*"

    if len(all_chars) == 0:
        return ""

    password = ""
    for i in range(length):
        random_char = random.choice(all_chars)
        password += random_char

    return password


def check_how_strong(password):
    points = 0

    if len(password) >= 8:
        points += 1

    if len(password) >= 12:
        points += 1

    has_big = False
    has_small = False
    has_number = False
    has_special = False

    for char in password:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            has_big = True
        if char in "abcdefghijklmnopqrstuvwxyz":
            has_small = True
        if char in "0123456789":
            has_number = True
        if char in "!@#$%^&*":
            has_special = True

    if has_big and has_small:
        points += 1

    if has_number:
        points += 1

    if has_special:
        points += 1

    if points >= 5:
        return "Очень сильный"
    elif points >= 3:
        return "Нормальный"
    elif points >= 1:
        return "Слабый"
    else:
        return "Очень слабый"


def make_many_passwords(how_many=5, length=8, special_chars=True, big_letters=True, numbers=True):
    passwords_list = []

    while len(passwords_list) < how_many:
        new_password = make_password(length, special_chars, big_letters, numbers)
        if new_password not in passwords_list:
            passwords_list.append(new_password)

    return passwords_list


print("Генератор паролей")
print("=================")

try:
    length_input = input("Какая длина пароля? (по умолчанию 8): ")
    if length_input == "":
        length_input = 8
    else:
        length_input = int(length_input)

    big_input = input("Нужны большие буквы? (да/нет): ")
    use_big = big_input.lower() in ['да', 'д', 'yes', 'y']

    numbers_input = input("Нужны цифры? (да/нет): ")
    use_numbers = numbers_input.lower() in ['да', 'д', 'yes', 'y']

    special_input = input("Нужны специальные знаки? (да/нет): ")
    use_special = special_input.lower() in ['да', 'д', 'yes', 'y']

    print("\nСоздаю один пароль...")
    password1 = make_password(length_input, use_special, use_big, use_numbers)
    print(f"Пароль: {password1}")
    strength = check_how_strong(password1)
    print(f"Надёжность: {strength}")

    print("\nСоздаю несколько паролей...")
    count_input = input("Сколько паролей создать? (по умолчанию 3): ")
    if count_input == "":
        count_input = 3
    else:
        count_input = int(count_input)

    passwords = make_many_passwords(count_input, length_input, use_special, use_big, use_numbers)

    print("\nГотовые пароли:")
    for i, pwd in enumerate(passwords, 1):
        strength_info = check_how_strong(pwd)
        print(f"{i}. {pwd} - {strength_info}")

except:
    print("Что-то пошло не так. Попробуйте ещё раз.")
