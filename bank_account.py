class BankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Your deposit is {self.__balance}"
        else:
            return "Your amount dont be the negative"
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return f"Your amount is bigger than your balance: {self.__balance}" 
        self.__balance -= amount
        return f"{self.owner} your transaction is done and your current balance is {self.__balance}"  
    
    def show_balance(self):
        return f"{self.owner} your balance is {self.__balance}"
    
    def transfer(self, amount, target_account):
        if amount < 0:
            return "Your amount must be positive"
        if amount < self.__balance:
            self.__balance -= amount
            target_account.deposit(amount)
            return f"You transferred f{amount} to {target_account.owner}"
        else:
            return "You dont have enough money"

my_bank = BankAccount("Dastan", 10000)
he_bank = BankAccount("Saken", 10000)
print(my_bank.deposit(6000))
print(my_bank.withdraw(5000))
print(my_bank.transfer(5000, he_bank))
print(my_bank.show_balance())
print(he_bank.show_balance())