class BankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
    
    def __str__(self):
        return f"Owner {self.owner} balance: {self._balance}"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Your deposit is {self._balance}"
        else:
            return "Your amount dont be the negative"
    
    def withdraw(self, amount):
        if amount > self._balance:
            return f"Your amount is bigger than your balance: {self._balance}" 
        self._balance -= amount
        return f"{self.owner} your transaction is done and your current balance is {self._balance}"  
    
    def show_balance(self):
        return f"{self.owner} your balance is {self._balance}"
    
    def transfer(self, amount, target_account):
        if amount < 0:
            return "Your amount must be positive"
        if amount < self._balance:
            self._balance -= amount
            target_account.deposit(amount)
            return f"You transferred {amount} to {target_account.owner}"
        else:
            return "You dont have enough money"

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
    
    def __str__(self):
        return f"Savings of {self.owner}, balance: {self._balance}, interest: {self.interest_rate*100}%"

def transfer_to_savings(main_account, savings_account, amount):
    if amount <= 0:
        return "Amount must be positive"
    if main_account._balance < amount:
        return "Not enough money on main balance"
    
    main_account.withdraw(amount)
    savings_account.deposit(amount)
    return f"Transferred {amount} from main to savings"

my_bank = BankAccount("Bob", 10000)
he_bank = BankAccount("Tom", 10000)
print(my_bank.deposit(6000))
print(my_bank.withdraw(5000))
print(my_bank.transfer(5000, he_bank))
print(my_bank.show_balance())
print(he_bank.show_balance())
my_savings = SavingsAccount(my_bank.owner, my_bank._balance, interest_rate=0.05)
my_savings.apply_interest()
print(my_bank.show_balance())
print(my_savings)
print(my_bank.show_balance())
transfer_to_savings(my_bank, my_savings, 1000)
print(my_bank)
print(my_savings)