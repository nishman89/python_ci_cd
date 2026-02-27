from .bank_account import BankAccount


class SavingsAccount(BankAccount):
    """A savings account that extends BankAccount with an interest rate."""

    def __init__(self, initial_balance: float, interest_rate: float):
        """Constructor — initialises the account with a balance and a fixed interest rate."""
        super().__init__(initial_balance)
        self._interest_rate = interest_rate

    def add_interest(self) -> None:
        """Calculate and deposit interest based on the current balance."""
        interest = self.get_balance() * self._interest_rate / 100
        self.deposit(interest)