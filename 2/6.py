class GameBank:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def __log_transaction(self, type_, amount):
        print(f"Транзакция: {type_} {amount}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__log_transaction("пополнение", amount)
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__log_transaction("снятие", amount)
            return True
        return False

    @property
    def balance(self):
        return self._balance