class City:
    def __init__(self, name="", region="", country="", population=0, postal_code="", phone_code=""):
        self._name = name
        self._region = region
        self._country = country
        self._population = population
        self._postal_code = postal_code
        self._phone_code = phone_code

    def input_data(self):
        self._name = input("Введите название города: ")
        self._region = input("Введите регион: ")
        self._country = input("Введите страну: ")
        self._population = int(input("Введите население: "))
        self._postal_code = input("Введите почтовый индекс: ")
        self._phone_code = input("Введите телефонный код: ")

    def display_data(self):
        print(f"Город: {self._name}")
        print(f"Регион: {self._region}")
        print(f"Страна: {self._country}")
        print(f"Население: {self._population}")
        print(f"Почтовый индекс: {self._postal_code}")
        print(f"Телефонный код: {self._phone_code}")

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def region(self):
        return self._region
    @region.setter
    def region(self, value):
        self._region = value

    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, value):
        self._country = value

    @property
    def population(self):
        return self._population
    @population.setter
    def population(self, value):
        self._population = value

    @property
    def postal_code(self):
        return self._postal_code
    @postal_code.setter
    def postal_code(self, value):
        self._postal_code = value

    @property
    def phone_code(self):
        return self._phone_code
    @phone_code.setter
    def phone_code(self, value):
        self._phone_code = value