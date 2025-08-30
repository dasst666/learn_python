import json
import os
from bank_app.errors import *
import functools
import time

class BankAccount():
    folder = "data"
    def __init__(self, owner, balance = 0, filename = "balance.json"):
        self.owner = owner
        os.makedirs(self.folder, exist_ok=True)
        self.filename = filename
        self._balance = self.load_balance() or balance
    
    def __str__(self):
        return f"Owner {self.owner} balance: {self._balance}"
    
    def log_operation(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] Вызов {func.__name__} с args={args[1:]}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"[LOG] Результат {func.__name__}: {result}")
            return result
        return wrapper
    
    def log_time(func):
        @functools.wraps(func)
        def timeit(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"[LOG] Время выполнения: {elapsed_time} s")
            return result
        return timeit
    
    def log_require_positive(func):
        @functools.wraps(func)
        def require_positive(*args, **kwargs):
            if args[1] < 0:
                print(f"[LOG] Сумма пополнения не может быть меньше нуля {args[1]}")
            result = func(*args, **kwargs)
            return result 
        return require_positive

    
    @log_require_positive
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Your deposit is {self._balance}"
        else:
            raise NegativeValueError(amount)
    
    @log_operation
    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        return f"{self.owner} your transaction is done and your current balance is {self._balance}"  
    
    @log_operation
    def show_balance(self):
        return f"{self.owner} your balance is {self._balance}"
    
    @log_time
    def transfer(self, amount, target_account):
        if amount < 0:
            raise NegativeValueError(amount)
        if amount <= self._balance:
            self._balance -= amount
            target_account.deposit(amount)
            self.save_transfer(target_account, amount)
            return f"You transferred {amount} to {target_account.owner}"
        else:
            raise InsufficientFundsError(self._balance, amount)
    
    @log_operation
    def transfer_to_savings(self, savings_account, amount):
        if amount < 0:
            raise NegativeValueError(amount)
        if self._balance < amount:
            return "Not enough money on main balance"
        
        self.withdraw(amount)
        savings_account.deposit(amount)
        return f"Transferred {amount} from main to savings"
    
    @log_operation
    def get_file_path(self):
        file_path = os.path.join(self.folder, f"{self.owner}_{self.filename}")
        return file_path
    
    # @log_operation
    def _load_data(self):
        if os.path.exists(self.get_file_path()):
            with open(self.get_file_path(), "r") as f:
                return json.load(f)
        else:
            return {"owner": self.owner, "balance": self._balance, "transfers": []}
    
    # @log_operation
    def _save_data(self, data):
        with open(self.get_file_path(), "w") as f:
            return json.dump(data, f, indent=4)
    
    # @log_operation
    def save_transfer(self, target_account, amount):
        data = self._load_data()
        transfer_data = {"transfer_to": target_account.owner, "transfer_amount": amount}
        data["transfers"].append(transfer_data)
        self._save_data(data)
    
    # @log_operation
    def save_balance(self):
        data = self._load_data()
        data["balance"] = self._balance
        self._save_data(data)
    
    @log_operation
    def load_balance(self, default = 0):
        if os.path.exists(self.get_file_path()):
            with open(self.get_file_path(), "r") as f:
                try:
                    data = json.load(f)
                    return data.get("balance", default)
                except json.JSONDecodeError:
                    return default
        return default
    
    @log_operation
    def transaction_history(self):
        data = self._load_data()
        for transfer in data.get("transfers", []):
            yield transfer

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

