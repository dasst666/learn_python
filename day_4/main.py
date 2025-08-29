from bank_account import *

def main():
    my_bank = BankAccount("Bob", 10000)
    he_bank = BankAccount("Tom", 10000)
    my_bank.deposit(5000)
    safe_action(my_bank.deposit, -5)
    print(my_bank)
    print(he_bank)
    my_bank.transfer(6000, he_bank)
    # my_bank.transfer(1000, he_bank)
    print(my_bank)
    print(he_bank)



    # gen = my_bank.transaction_history()
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))

    # print(my_bank.deposit(10000))
    # print(my_bank.withdraw(5000))
    # print(my_bank.transfer(5000, he_bank))
    # print(my_bank.show_balance())
    # print(he_bank.show_balance())
    # my_savings = SavingsAccount(my_bank.owner, my_bank._balance, interest_rate=0.05)
    # my_savings.apply_interest()
    # print(my_bank.show_balance())
    # print(my_savings)
    # print(my_bank.show_balance())
    # my_bank.transfer_to_savings(my_savings, 1000)
    # print(my_bank)
    # print(my_savings)
    # safe_action(my_bank.deposit, -5)
    # safe_action(my_bank.withdraw, 75000)
    # safe_action(my_bank.deposit, "test")
    # my_bank.save_balance()
    # print(my_bank.load_balance())

if __name__ == "__main__":
    main()