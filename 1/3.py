class Country:
    def __init__(self, name="", continent="", population=0, phone_code="", capital="", cities=None):
        self._name = name
        self._continent = continent
        self._population = population
        self._phone_code = phone_code
        self._capital = capital
        self._cities = cities if cities else []

    def input_data(self):
        self._name = input("Введите страну: ")
        self._continent = input("Введите континент: ")
        self._population = int(input("Введите население: "))
        self._phone_code = input("Введите телефонный код: ")
        self._capital = input("Введите столицу: ")

        n = int(input("Сколько городов добавить? "))
        self._cities = []
        for i in range(n):
            city = input(f"Город {i + 1}: ")
            self._cities.append(city)

    def display_data(self):
        print(f"Страна: {self._name}")
        print(f"Континент: {self._continent}")
        print(f"Население: {self._population}")
        print(f"Телефонный код: {self._phone_code}")
        print(f"Столица: {self._capital}")
        print(f"Города: {', '.join(self._cities)}")

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def continent(self):
        return self._continent
    @continent.setter
    def continent(self, value):
        self._continent = value

    @property
    def population(self):
        return self._population
    @population.setter
    def population(self, value):
        self._population = value

    @property
    def phone_code(self):
        return self._phone_code
    @phone_code.setter
    def phone_code(self, value):
        self._phone_code = value

    @property
    def capital(self):
        return self._capital
    @capital.setter
    def capital(self, value):
        self._capital = value

    @property
    def cities(self):
        return self._cities
    @cities.setter
    def cities(self, value):
        self._cities = value