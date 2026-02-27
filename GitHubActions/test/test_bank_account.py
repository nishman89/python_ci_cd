import pytest
from main.bank_account import BankAccount


class TestBankAccount:

    def test_initial_balance(self):
        account = BankAccount(100.0)
        assert account.get_balance() == 100.0

    def test_initial_balance_zero(self):
        account = BankAccount(0.0)
        assert account.get_balance() == 0.0

    def test_deposit_increases_balance(self):
        account = BankAccount(100.0)
        account.deposit(50.0)
        assert account.get_balance() == 150.0

    def test_deposit_zero(self):
        account = BankAccount(100.0)
        account.deposit(0.0)
        assert account.get_balance() == 100.0

    def test_multiple_deposits(self):
        account = BankAccount(0.0)
        account.deposit(100.0)
        account.deposit(200.0)
        assert account.get_balance() == 300.0

    def test_withdraw_decreases_balance(self):
        account = BankAccount(100.0)
        account.withdraw(30.0)
        assert account.get_balance() == 70.0

    def test_withdraw_full_balance(self):
        account = BankAccount(100.0)
        account.withdraw(100.0)
        assert account.get_balance() == 0.0

    def test_withdraw_zero(self):
        account = BankAccount(100.0)
        account.withdraw(0.0)
        assert account.get_balance() == 100.0

    def test_withdraw_overdraft(self):
        account = BankAccount(50.0)
        account.withdraw(100.0)
        assert account.get_balance() == -50.0

    def test_multiple_withdrawals(self):
        account = BankAccount(200.0)
        account.withdraw(50.0)
        account.withdraw(50.0)
        assert account.get_balance() == 100.0

    def test_deposit_and_withdraw(self):
        account = BankAccount(100.0)
        account.deposit(50.0)
        account.withdraw(30.0)
        assert account.get_balance() == 120.0