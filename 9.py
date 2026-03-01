class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def display_info(self):
        return f"Имя: {self.__name}, Возраст: {self.__age}"


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.__position = position

    def get_position(self):
        return self.__position

    def display_info(self):
        return f"{super().display_info()}, Должность: {self.__position}"


class Manager(Employee):
    def __init__(self, name, age, position):
        super().__init__(name, age, position)
        self.__team = []

    def add_to_team(self, employee):
        if employee not in self.__team:
            self.__team.append(employee)
            print(f"Сотрудник {employee.get_name()} добавлен в команду менеджера {self.get_name()}")
        else:
            print(f"Сотрудник {employee.get_name()} уже в команде")

    def display_team_info(self):
        if not self.__team:
            return f"У менеджера {self.get_name()} пока нет подчиненных"

        team_info = f"Команда менеджера {self.get_name()}:\n"
        for emp in self.__team:
            team_info += f"  - {emp.get_name()} ({emp.get_position()})\n"
        return team_info

    def display_info(self):
        return f"{super().display_info()} (Менеджер, команда: {len(self.__team)} чел.)"

    def get_team(self):
        return self.__team.copy()


def main():
    employees = []
    managers = []

    print("=" * 50)
    print("Программа учета сотрудников компании")
    print("Команды: add - добавить сотрудника, assign - назначить в команду")
    print("         list - показать всех, exit - выход")
    print("=" * 50)

    while True:
        try:
            command = input("\nВведите команду: ").strip().lower()

            if command == "exit":
                print("Программа завершена")
                break

            elif command == "add":
                name = input("Введите имя: ").strip()
                if not name:
                    print("Ошибка: имя не может быть пустым")
                    continue

                try:
                    age = int(input("Введите возраст: ").strip())
                    if age <= 0 or age > 120:
                        print("Ошибка: возраст должен быть от 1 до 120")
                        continue
                except ValueError:
                    print("Ошибка: возраст должен быть числом")
                    continue

                position = input("Введите должность: ").strip()
                if not position:
                    print("Ошибка: должность не может быть пустой")
                    continue

                is_manager = input("Это менеджер? (да/нет): ").strip().lower()

                if is_manager == "да":
                    new_employee = Manager(name, age, position)
                    managers.append(new_employee)
                else:
                    new_employee = Employee(name, age, position)

                employees.append(new_employee)
                print(f"Сотрудник {name} успешно добавлен!")

            elif command == "assign":
                if not employees:
                    print("Ошибка: нет сотрудников в системе")
                    continue

                if not managers:
                    print("Ошибка: в системе нет менеджеров")
                    continue

                print("\nДоступные менеджеры:")
                for i, man in enumerate(managers, 1):
                    print(f"{i}. {man.get_name()} ({man.get_position()})")

                manager_name = input("\nВведите имя менеджера: ").strip()
                employee_name = input("Введите имя сотрудника: ").strip()

                found_manager = None
                for man in managers:
                    if man.get_name().lower() == manager_name.lower():
                        found_manager = man
                        break

                if not found_manager:
                    print("Ошибка: менеджер с таким именем не найден")
                    continue

                found_employee = None
                for emp in employees:
                    if emp.get_name().lower() == employee_name.lower():
                        found_employee = emp
                        break

                if not found_employee:
                    print("Ошибка: сотрудник с таким именем не найден")
                    continue

                if found_employee == found_manager:
                    print("Ошибка: менеджер не может добавить сам себя в команду")
                    continue

                found_manager.add_to_team(found_employee)

            elif command == "list":
                if not employees:
                    print("В системе нет сотрудников")
                else:
                    print("\n" + "=" * 50)
                    print("СПИСОК ВСЕХ СОТРУДНИКОВ")
                    print("=" * 50)

                    for emp in employees:
                        print(emp.display_info())

                        if isinstance(emp, Manager):
                            team = emp.get_team()
                            if team:
                                print("  Подчиненные:")
                                for subordinate in team:
                                    print(f"    - {subordinate.get_name()} ({subordinate.get_position()})")
                            else:
                                print("  Подчиненных пока нет")
                        print("-" * 30)

            else:
                print("Неизвестная команда. Используйте: add, assign, list, exit")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

