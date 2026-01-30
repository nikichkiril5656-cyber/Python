class Employee:
    def __init__(self, name, position):
        self.__name = name
        self.__position = position


    def display_info(self):
        print(f"Имя: {self.__name}, Должность: {self.__position}")

class Team:
    def __init__(self):
        self.team_members=[]

    def add_members(self,employee):
        self.team_members.append(employee)

    def show_team(self):
        if not self.team_members:
            print("В команде нет сотрудников.")
            return
        for member in self.team_members:
            if hasattr(member, 'name') and hasattr(member, 'position'):
                print(f"Сотрудник: {member.name}, Должность: {member.position}")
            else:
                print("Объект без атрибутов name и position")


my_team=Team()
my_team.show_team()
emp1=Employee("Иван Петров", "Разработчик")
emp2=Employee("Тимофей","Сис. Админ")
my_team.add_members(emp1)
my_team.add_members(emp2)
my_team.show_team   ()