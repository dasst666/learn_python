class NegativeValueError(Exception):
    def __init__(self, amount):
        super().__init__(f"Cумма {amount} отрицательная")

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Недостаточно средств на счете: {balance}, вы пытаетесь снять {amount}")