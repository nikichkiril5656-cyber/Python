import random
import time

class Animal:
    def __init__(self, name, age, weight):
        self._name = name
        self._age = age
        self._weight = weight
        self._hunger = 50
        self._health = 100
        self._mood = 50
        self._is_sleeping = False

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def weight(self):
        return self._weight

    @property
    def hunger(self):
        return self._hunger
    @hunger.setter
    def hunger(self, value):
        self._hunger = max(0, min(100, value))

    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, value):
        self._health = max(0, min(100, value))

    @property
    def mood(self):
        return self._mood
    @mood.setter
    def mood(self, value):
        self._mood = max(0, min(100, value))

    @property
    def is_sleeping(self):
        return self._is_sleeping
    @is_sleeping.setter
    def is_sleeping(self, value):
        self._is_sleeping = value

    def _change_hunger(self, delta):
        self.hunger = self.hunger + delta

    def _change_health(self, delta):
        self.health = self.health + delta

    def _change_mood(self, delta):
        self.mood = self.mood + delta

    def make_sound(self):
        if self._is_sleeping:
            return f"{self._name} тихо посапывает во сне..."
        return f"{self._name} издает звук"

    def move(self):
        if self._is_sleeping:
            return f"{self._name} спит и не двигается"
        return f"{self._name} перемещается"

    def eat(self, food_amount=20):
        if self._is_sleeping:
            print(f"{self._name} спит и не ест.")
            return False

        if self._hunger <= 0:
            print(f"{self._name} не голоден.")
            return False

        self._change_hunger(-food_amount)
        self._change_health(5)
        self._change_mood(10)

        print(f"{self._name} покушал. Голод: {self._hunger}/100")
        return True

    def sleep(self):
        self.is_sleeping = True
        print(f"{self._name} уснул.")
        self._change_health(5)
        self._change_mood(5)

    def wake_up(self):
        if self._is_sleeping:
            self.is_sleeping = False
            print(f"{self._name} проснулся.")
        else:
            print(f"{self._name} и не спал.")

    def play(self):
        if self._is_sleeping:
            print(f"{self._name} спит и не может играть.")
            return False

        if self._health < 30:
            print(f"{self._name} слишком болен для игр.")
            return False

        self._change_mood(20)
        self._change_hunger(15)
        self._change_health(-5)

        print(f"{self._name} поиграл и счастлив! Настроение: {self._mood}/100")
        return True

    def get_status(self):
        status = f"\n=== {self._name} ({self.__class__.__name__}) ===\n"
        status += f"Возраст: {self._age} лет\n"
        status += f"Вес: {self._weight} кг\n"
        status += f"Голод: {self._hunger}/100\n"
        status += f"Здоровье: {self._health}/100\n"
        status += f"Настроение: {self._mood}/100\n"
        status += f"Состояние: {'Спит' if self._is_sleeping else 'Бодрствует'}"
        return status

    def special_action(self):
        print(f"{self._name} выполняет обычное действие")

    def __str__(self):
        return f"{self._name} - {self.__class__.__name__}"


class Lion(Animal):
    def __init__(self, name, age, weight, mane_size=10):
        super().__init__(name, age, weight)
        self._mane_size = mane_size
        self._pride_size = 1

    @property
    def mane_size(self):
        return self._mane_size

    @mane_size.setter
    def mane_size(self, value):
        if value > 0:
            self._mane_size = value

    @property
    def pride_size(self):
        return self._pride_size

    @pride_size.setter
    def pride_size(self, value):
        if value > 0:
            self._pride_size = value

    def make_sound(self):
        if self._is_sleeping:
            return f"{self._name} тихо похрапывает во сне..."
        return f"{self._name} громко рычит: РРРРРРРРР!"

    def move(self):
        if self._is_sleeping:
            return f"{self._name} спит и не двигается"
        return f"{self._name} величественно шагает по вольеру"

    def special_action(self):
        if self._is_sleeping:
            print(f"{self._name} спит и не охотится.")
            return False

        if self._hunger < 30:
            print(f"{self._name} не очень голоден для охоты.")
            return False

        success = random.random() > 0.3
        if success:
            print(f"{self._name} успешно поохотился и сыт!")
            self.hunger = 0
            self._change_mood(20)
        else:
            print(f"{self._name} не поймал добычу...")
            self._change_hunger(10)
            self._change_mood(-10)

        return success


class Elephant(Animal):
    def __init__(self, name, age, weight, trunk_length=2):
        super().__init__(name, age, weight)
        self._trunk_length = trunk_length
        self._water_consumed = 0

    @property
    def trunk_length(self):
        return self._trunk_length

    @trunk_length.setter
    def trunk_length(self, value):
        if value > 0:
            self._trunk_length = value

    @property
    def water_consumed(self):
        return self._water_consumed

    @water_consumed.setter
    def water_consumed(self, value):
        if value >= 0:
            self._water_consumed = value

    def make_sound(self):
        if self._is_sleeping:
            return f"{self._name} трубит во сне: Ту-у-у-у..."
        return f"{self._name} трубит: Ту-уууууу!"

    def move(self):
        if self._is_sleeping:
            return f"{self._name} спит стоя"
        return f"{self._name} медленно и тяжело ступает"

    def special_action(self):
        if self._is_sleeping:
            print(f"{self._name} спит и не может брызгаться водой.")
            return

        print(f"{self._name} брызгается водой из хобота!")
        self.water_consumed += 10
        self._change_mood(15)

    def drink(self, liters):
        if self._is_sleeping:
            print(f"{self._name} спит и не пьет.")
            return

        self.water_consumed += liters
        self._change_hunger(-(liters // 2))
        print(f"{self._name} выпил {liters} литров воды")


class Monkey(Animal):
    def __init__(self, name, age, weight, tail_length=50):
        super().__init__(name, age, weight)
        self._tail_length = tail_length
        self._bananas_eaten = 0

    @property
    def tail_length(self):
        return self._tail_length

    @tail_length.setter
    def tail_length(self, value):
        if value > 0:
            self._tail_length = value

    @property
    def bananas_eaten(self):
        return self._bananas_eaten

    @bananas_eaten.setter
    def bananas_eaten(self, value):
        if value >= 0:
            self._bananas_eaten = value

    def make_sound(self):
        if self._is_sleeping:
            return f"{self._name} посапывает: у-у-у..."
        return f"{self._name} ухает: У-у-у-у-у!"

    def move(self):
        if self._is_sleeping:
            return f"{self._name} свернулся калачиком и спит"
        return f"{self._name} скачет по веткам и кувыркается"

    def special_action(self):
        if self._is_sleeping:
            print(f"{self._name} спит и не лезет на дерево.")
            return False

        if self._health < 40:
            print(f"{self._name} слишком слаб, чтобы лазать.")
            return False

        print(f"{self._name} ловко залез на дерево!")
        self._change_mood(25)
        self._change_hunger(10)
        return True

    def eat_banana(self):
        if self._is_sleeping:
            print(f"{self._name} спит и не ест банан.")
            return

        self.bananas_eaten += 1
        self._change_hunger(-15)
        self._change_mood(20)
        print(f"{self._name} съел банан! Всего бананов: {self._bananas_eaten}")


class Penguin(Animal):
    def __init__(self, name, age, weight, swim_speed=10):
        super().__init__(name, age, weight)
        self._swim_speed = swim_speed
        self._swim_distance = 0

    @property
    def swim_speed(self):
        return self._swim_speed

    @swim_speed.setter
    def swim_speed(self, value):
        if value > 0:
            self._swim_speed = value

    @property
    def swim_distance(self):
        return self._swim_distance

    @swim_distance.setter
    def swim_distance(self, value):
        if value >= 0:
            self._swim_distance = value

    def make_sound(self):
        if self._is_sleeping:
            return f"{self._name} тихо попискивает во сне"
        return f"{self._name} кричит: Кря-кря-кря!"

    def move(self):
        if self._is_sleeping:
            return f"{self._name} стоит на льду и спит"
        return f"{self._name} неуклюже переваливается"

    def special_action(self):
        if self._is_sleeping:
            print(f"{self._name} спит и не плавает.")
            return

        distance = random.randint(10, 50)

        if self._health < 30:
            print(f"{self._name} слишком болен для плавания.")
            return

        self.swim_distance += distance
        self._change_hunger(distance // 2)
        self._change_health(-(distance // 10))
        self._change_mood(distance // 2)

        print(f"{self._name} проплыл {distance} метров! Общая дистанция: {self.swim_distance}")


class Zoo:
    def __init__(self, name):
        self._name = name
        self._animals = []
        self._visitors = 0
        self._money = 1000

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value

    @property
    def animals(self):
        return self._animals.copy()

    @property
    def animals_count(self):
        return len(self._animals)

    @property
    def visitors(self):
        return self._visitors

    @visitors.setter
    def visitors(self, value):
        if value >= 0:
            self._visitors = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        if value >= 0:
            self._money = value

    def _add_visitors(self, count):
        self.visitors += count

    def _add_money(self, amount):
        self.money += amount

    def add_animal(self, animal):
        self._animals.append(animal)
        print(f"Животное {animal} добавлено в зоопарк!")

    def remove_animal(self, animal_name):
        for animal in self._animals:
            if animal.name.lower() == animal_name.lower():
                self._animals.remove(animal)
                print(f"Животное {animal} удалено из зоопарка.")
                return True
        print(f"Животное с именем {animal_name} не найдено.")
        return False

    def feed_all(self):
        print("\n=== Кормление всех животных ===")
        for animal in self._animals:
            animal.eat(15)
            time.sleep(1)

    def show_all_animals(self):
        if not self._animals:
            print("В зоопарке пока нет животных!")
            return

        print(f"\n=== Животные в зоопарке '{self._name}' ===")
        for i, animal in enumerate(self._animals, 1):
            print(f"{i}. {animal} - {animal.make_sound()}")

    def animal_interaction(self, animal_name, action):
        for animal in self._animals:
            if animal.name.lower() == animal_name.lower():
                print(f"\nВзаимодействие с {animal.name}:")

                if action == "sound":
                    print(animal.make_sound())
                elif action == "move":
                    print(animal.move())
                elif action == "play":
                    animal.play()
                elif action == "feed":
                    try:
                        amount = int(input("Сколько корма дать? (10-30): "))
                        animal.eat(amount)
                    except:
                        animal.eat(15)
                elif action == "status":
                    print(animal.get_status())
                elif action == "special":
                    animal.special_action()
                elif action == "sleep":
                    animal.sleep()
                elif action == "wake":
                    animal.wake_up()
                else:
                    print("Неизвестное действие")

                return True

        print(f"Животное {animal_name} не найдено")
        return False

    def simulate_day(self):
        print(f"\n=== Начинается новый день в зоопарке '{self._name}' ===")

        for animal in self._animals:
            animal.wake_up()
            time.sleep(0.5)

        self.feed_all()

        print("\n=== Животные активны ===")
        for animal in self._animals:
            print(animal.move())
            print(animal.make_sound())
            time.sleep(0.5)

        print("\n=== Животные занимаются своими делами ===")
        for animal in self._animals:
            if random.random() > 0.5:
                animal.special_action()
            time.sleep(0.5)

        visitors_today = random.randint(50, 200)
        self._add_visitors(visitors_today)
        self._add_money(visitors_today * 5)
        print(f"\nСегодня зоопарк посетило {self.visitors} человек. Денег: {self.money}")

        print("\n=== Вечер, животные готовятся ко сну ===")
        for animal in self._animals:
            animal.sleep()
            time.sleep(0.5)

    def run(self):
        simba = Lion("Симба", 5, 190, 15)
        dumbo = Elephant("Дамбо", 10, 5000, 2)
        abu = Monkey("Абу", 3, 15, 40)
        skipper = Penguin("Шкипер", 2, 25, 12)

        self.add_animal(simba)
        self.add_animal(dumbo)
        self.add_animal(abu)
        self.add_animal(skipper)

        while True:
            print("\n" + "=" * 40)
            print("ГЛАВНОЕ МЕНЮ ЗООПАРКА")
            print("=" * 40)
            print("1. Показать всех животных")
            print("2. Покормить всех животных")
            print("3. Взаимодействовать с животным")
            print("4. Симулировать день")
            print("5. Добавить новое животное")
            print("6. Показать статус зоопарка")
            print("0. Выйти")

            choice = input("Выберите действие: ")

            if choice == "1":
                self.show_all_animals()

            elif choice == "2":
                self.feed_all()

            elif choice == "3":
                self.show_all_animals()
                animal_name = input("Введите имя животного: ")
                print("\nДоступные действия:")
                print("- sound (издать звук)")
                print("- move (двигаться)")
                print("- play (играть)")
                print("- feed (кормить)")
                print("- special (особое действие)")
                print("- sleep (усыпить)")
                print("- wake (разбудить)")
                print("- status (статус)")
                action = input("Введите действие: ")
                self.animal_interaction(animal_name, action)

            elif choice == "4":
                self.simulate_day()

            elif choice == "5":
                print("Добавление нового животного:")
                name = input("Имя: ")
                try:
                    age = int(input("Возраст: "))
                    weight = float(input("Вес: "))
                except:
                    print("Ошибка ввода! Животное не создано.")
                    continue

                print("Тип животного:")
                print("1. Лев")
                print("2. Слон")
                print("3. Обезьяна")
                print("4. Пингвин")
                print("5. Обычное животное")
                animal_type = input("Выберите тип (1-5): ")

                if animal_type == "1":
                    try:
                        mane_size = int(input("Размер гривы (см): "))
                    except:
                        mane_size = 15
                    animal = Lion(name, age, weight, mane_size)
                elif animal_type == "2":
                    try:
                        trunk_length = int(input("Длина хобота (м): "))
                    except:
                        trunk_length = 2
                    animal = Elephant(name, age, weight, trunk_length)
                elif animal_type == "3":
                    try:
                        tail_length = int(input("Длина хвоста (см): "))
                    except:
                        tail_length = 50
                    animal = Monkey(name, age, weight, tail_length)
                elif animal_type == "4":
                    try:
                        swim_speed = int(input("Скорость плавания (км/ч): "))
                    except:
                        swim_speed = 10
                    animal = Penguin(name, age, weight, swim_speed)
                else:
                    animal = Animal(name, age, weight)

                self.add_animal(animal)

            elif choice == "6":
                print(f"\n=== Статус зоопарка '{self.name}' ===")
                print(f"Всего животных: {len(self._animals)}")
                print(f"Посетителей сегодня: {self.visitors}")
                print(f"Денег в кассе: {self.money}")
                print("\nСтатус животных:")
                for animal in self._animals:
                    mood = animal.mood
                    health = animal.health
                    status_emoji = "😊" if mood > 70 else "😐" if mood > 40 else "😞"
                    health_emoji = "💚" if health > 70 else "💛" if health > 40 else "❤️"
                    print(f"- {animal.name}: здоровье {health}% {health_emoji}, голод {animal.hunger}% {status_emoji}")

            elif choice == "0":
                print("До свидания! Спасибо за посещение зоопарка!")
                break

            else:
                print("Неверный выбор, попробуйте снова")


my_zoo = Zoo("Чудо-зоопарк")
my_zoo.run()