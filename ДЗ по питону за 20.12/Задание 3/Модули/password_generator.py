import random
import string
def generate_password(lenght, use_upper=True,use_special=True, use_lower=True, use_digits=True):
    chars=''
    if use_lower:
        chars+=string.ascii_lowercase
    if use_digits:
        chars+=string.digits
    if use_upper:
        chars+=string.ascii_uppercase
    if use_special:
        chars+="!@#$%^&*()"

    if not chars:
        return ""

    password=""
    for _ in range(lenght):
        password+=random.choice(chars)
    return password

def check_password_strength(password):
    if len(password) < 8:
        return "Слабый"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()" for c in password)

    score = has_upper + has_lower + has_digit + has_special
    if score == 4:
        return "Очень надежный"
    elif score >= 2:
        return "Надежный"
    else:
        return "Слабый"


def generate_unique_passwords(count, length=12):
    passwords = set()
    while len(passwords) < count:
        pwd = generate_password(length)
        if pwd:
            passwords.add(pwd)
    return list(passwords)