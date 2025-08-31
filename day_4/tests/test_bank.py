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
    deposit_amount = 5000
    before_balance = my_account._balance
    my_account.deposit(deposit_amount)
    assert my_account._balance == before_balance + deposit_amount

def test_deposit_negative(my_account):
    # Тест на поплнение отрицательной суммы
    with pytest.raises(NegativeValueError):
        my_account.deposit(-5000)

def test_withdraw_decrease(my_account):
    # Тест на снятие денег
    withdraw_amount = 999
    before_withdraw_balance = my_account._balance
    my_account.withdraw(withdraw_amount)
    assert my_account._balance == (before_withdraw_balance - withdraw_amount)

def test_withdraw_error(my_account):
    # Тест на снятие денег больше чем имеется на счету
    withdraw_bigger = my_account._balance + 10
    with pytest.raises(InsufficientFundsError):
        my_account.withdraw(withdraw_bigger)

def test_transfer(my_account, other_account):
    # Тест на перевод денег на другой аккаунт
    transfer_amount = 5000
    before_other_acount = other_account._balance
    my_account.transfer(transfer_amount, other_account)
    assert other_account._balance == before_other_acount + transfer_amount

def test_transfer_error(my_account, other_account):
    # Тест на перевод денег больше чем имеется на счету
    transfer_bigger = my_account._balance + 10
    with pytest.raises(InsufficientFundsError):
        my_account.transfer(transfer_bigger, other_account)