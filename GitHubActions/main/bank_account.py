class BankAccount:

    def __init__(self, initial_balance: float):
        self._balance = initial_balance

    def deposit(self, amount: float) -> None:
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        self._balance -= amount

    def get_balance(self) -> float:
        return self._balance