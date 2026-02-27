import pytest
from main.savings_account import SavingsAccount
from main.bank_account import BankAccount

class TestSavingsAccount:

    def test_initial_balance(self):
        account = SavingsAccount(1000.0, 5.0)
        assert account.get_balance() == 1000.0

    def test_interest_rate_stored(self):
        account = SavingsAccount(1000.0, 5.0)
        assert account._interest_rate == 5.0

    def test_add_interest_correct_amount(self):
        account = SavingsAccount(1000.0, 5.0)
        account.add_interest()
        assert account.get_balance() == 1050.0

    def test_add_interest_zero_rate(self):
        account = SavingsAccount(1000.0, 0.0)
        account.add_interest()
        assert account.get_balance() == 1000.0

    def test_add_interest_zero_balance(self):
        account = SavingsAccount(0.0, 5.0)
        account.add_interest()
        assert account.get_balance() == 0.0

    def test_add_interest_multiple_times(self):
        account = SavingsAccount(1000.0, 10.0)
        account.add_interest()  # 1000 + 100 = 1100
        account.add_interest()  # 1100 + 110 = 1210
        assert account.get_balance() == 1210.0

    def test_add_interest_fractional_rate(self):
        account = SavingsAccount(200.0, 2.5)
        account.add_interest()
        assert account.get_balance() == 205.0

    def test_inherits_deposit(self):
        account = SavingsAccount(500.0, 5.0)
        account.deposit(100.0)
        assert account.get_balance() == 600.0

    def test_inherits_withdraw(self):
        account = SavingsAccount(500.0, 5.0)
        account.withdraw(100.0)
        assert account.get_balance() == 400.0

    def test_deposit_then_add_interest(self):
        account = SavingsAccount(500.0, 10.0)
        account.deposit(500.0)   # balance = 1000
        account.add_interest()   # interest = 100
        assert account.get_balance() == 1100.0

    def test_is_instance_of_bank_account(self):
        account = SavingsAccount(1000.0, 5.0)
        assert isinstance(account, BankAccount)