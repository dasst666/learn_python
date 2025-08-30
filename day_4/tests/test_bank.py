import pytest
from bank_app.bank_account import BankAccount
from bank_app.errors import *

@pytest.fixture
def my_account():
    return BankAccount("Tom", 10000)

@pytest.fixture
def other_account():
    return BankAccount("Jerry", 10000)

def test_deposit_increase(my_account):
    # Тест на пополнение аккаунта
    my_account.deposit(5000)
    assert my_account._balance == 15000

def test_deposit_negative(my_account):
    # Тест на поплнение отрицательной суммы
    with pytest.raises(NegativeValueError):
        my_account.deposit(-5000)

def test_withdraw_decrease(my_account):
    # Тест на снятие денег
    before_withdraw_balance = my_account._balance
    my_account.withdraw(999)
    assert my_account._balance == (before_withdraw_balance - 999)

def test_withdraw_error(my_account):
    # Тест на снятие денег больше чем имеется на счету
    withdraw_bigger = my_account._balance + 10
    with pytest.raises(InsufficientFundsError):
        my_account.withdraw(withdraw_bigger)
