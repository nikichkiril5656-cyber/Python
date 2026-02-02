class Human:

    def __init__(self):
        self._full_name = ""
        self._birth_date = ""
        self._phone = ""
        self._city = ""
        self._country = ""
        self._address = ""

    def input_info(self):
        self._full_name=input("Введите ФИО: ")
        self._birth_date=input("Введите дату рождения: ")
        self._phone=input("Введите телефон: ")
        self._city=input("Введите город: ")
        self._country=input("Введите страну: ")
        self._address=input("Введите адрес: ")

    def display_data(self):
        print("Данные о человеке:\n"
              f"ФИО: {self._full_name}\n"
              f"Дата рождения: {self._birth_date}\n"
              f"Телефон: {self._phone}\n"
              f"Город: {self._city}\n"
              f"Страна: {self._country}\n"
              f"Адрес: {self._address}")

    @property
    def full_name(self):
        return self._full_name
    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    @property
    def birth_date(self):
        return self._birth_date
    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        self._city = value

    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, value):
        self._country = value

    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, value):
        self._address = value

