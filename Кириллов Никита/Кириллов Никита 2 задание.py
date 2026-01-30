class Book:
    def __init__(self, name, author, year):
        self.__name = name
        self.__author = author
        self.__year = year

    def display_info(self):
        print(f"Имя: {self.__name}, Автор: {self.__author}, Год: {self.__year}")

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year):
        self.__year = year


book1 = Book("Мёртвые души", "Гоголь", "Какой-то\n")
book1.display_info()
book1.year = 2020
book1.name = "Смерть в нищите"
book1.author = "Тик Ток"
book1.display_info()