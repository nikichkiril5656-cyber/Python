from math import gcd


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть 0")
        self._numerator = numerator
        self._denominator = denominator
        self._simplify()

    def _simplify(self):
        if self._numerator == 0:
            self._denominator = 1
            return
        common = gcd(abs(self._numerator), abs(self._denominator))
        self._numerator //= common
        self._denominator //= common
        if self._denominator < 0:
            self._numerator = -self._numerator
            self._denominator = -self._denominator

    def input_data(self):
        self._numerator = int(input("Числитель: "))
        denominator = int(input("Знаменатель: "))
        if denominator == 0:
            raise ValueError("Знаменатель не может быть 0")
        self._denominator = denominator
        self._simplify()

    def display_data(self):
        print(f"Дробь: {self._numerator}/{self._denominator}")

    @property
    def numerator(self):
        return self._numerator
    @numerator.setter
    def numerator(self, value):
        self._numerator = value
        self._simplify()

    @property
    def denominator(self):
        return self._denominator
    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError("Знаменатель не может быть 0")
        self._denominator = value
        self._simplify()

    def __add__(self, other):
        if isinstance(other, Fraction):
            num = self._numerator * other._denominator + other._numerator * self._denominator
            den = self._denominator * other._denominator
            return Fraction(num, den)
        return self + Fraction(other, 1)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            num = self._numerator * other._denominator - other._numerator * self._denominator
            den = self._denominator * other._denominator
            return Fraction(num, den)
        return self - Fraction(other, 1)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self._numerator * other._numerator, self._denominator * other._denominator)
        return Fraction(self._numerator * other, self._denominator)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other._numerator == 0:
                raise ValueError("Деление на ноль")
            return Fraction(self._numerator * other._denominator, self._denominator * other._numerator)

        if other == 0:
            raise ValueError("Деление на ноль")
        return Fraction(self._numerator, self._denominator * other)

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"
