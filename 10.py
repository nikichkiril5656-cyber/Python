from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

    def hypotenuse(self):
        return math.sqrt(self.base ** 2 + self.height ** 2)

    def perimeter(self):
        return self.base + self.height + self.hypotenuse()


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4)

print(f"Площадь круга: {circle.area():.1f}")
print(f"Длина окружности круга: {circle.circumference():.2f}")
print(f"Диаметр круга: {circle.diameter()}")

print(f"\nПлощадь прямоугольника: {rectangle.area()}")
print(f"Периметр прямоугольника: {rectangle.perimeter()}")
print(f"Диагональ прямоугольника: {rectangle.diagonal():.2f}")

print(f"\nПлощадь треугольника: {triangle.area()}")
print(f"Гипотенуза треугольника: {triangle.hypotenuse()}")
print(f"Периметр треугольника: {triangle.perimeter():.2f}")