import json
import os
from errors import *
class BankAccount():
    folder = "data"
    def __init__(self, owner, balance = 0, filename = "balance.json"):
        self.owner = owner
        os.makedirs(self.folder, exist_ok=True)
        self.filename = filename
        self._balance = self.load_balance() or balance
    
    def __str__(self):
        return f"Owner {self.owner} balance: {self._balance}"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Your deposit is {self._balance}"
        else:
            raise NegativeValueError(amount)
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        return f"{self.owner} your transaction is done and your current balance is {self._balance}"  
    
    def show_balance(self):
        return f"{self.owner} your balance is {self._balance}"
    
    def transfer(self, amount, target_account):
        if amount < 0:
            raise NegativeValueError(amount)
        if amount < self._balance:
            self._balance -= amount
            target_account.deposit(amount)
            self.save_transfer(target_account, amount)
            return f"You transferred {amount} to {target_account.owner}"
        else:
            raise InsufficientFundsError(self._balance, amount)
    
    def transfer_to_savings(self, savings_account, amount):
        if amount < 0:
            raise NegativeValueError(amount)
        if self._balance < amount:
            return "Not enough money on main balance"
        
        self.withdraw(amount)
        savings_account.deposit(amount)
        return f"Transferred {amount} from main to savings"
    
    # @property сделать если что
    def get_file_path(self):
        file_path = os.path.join(self.folder, f"{self.owner}_{self.filename}")
        return file_path
    
    def save_transfer(self, target_account, amount):
        with open(self.get_file_path(), "w") as f:
            json.dump({"transfer_to": target_account.owner, "transfer_amount": amount}, f)
    
    def save_balance(self):
        with open(self.get_file_path(), "w") as f:
            json.dump({"owner": self.owner, "balance": self._balance}, f)
    
    def load_balance(self, default = 0):
        if os.path.exists(self.get_file_path()):
            with open(self.get_file_path(), "r") as f:
                data = json.load(f)
                return data.get("balance", default)
        return default

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
    
    def __str__(self):
        return f"Savings of {self.owner}, balance: {self._balance}, interest: {self.interest_rate*100}%"


def safe_action(action, *args):
    try:
        return action(*args)
    except (NegativeValueError, InsufficientFundsError) as e:
        print(f"Ошибка при операции {e}")
    except Exception as e:
        print(f"Неожиданная ошибка")

# try:
#     my_bank.deposit(-6000)
# except NegativeValueError as e:
#     print(f"Ошибка {e}")
# try:
#     print(my_bank.withdraw(85000))
# except InsufficientFundsError as e:
#     print(f"Ошибка {e}")

