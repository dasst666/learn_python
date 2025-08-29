# Train and use iterators and generators but i dont know how to use in real life cases

nums = []
for i in range(10):
    nums.append(i)


it = iter(nums)
print(next(it))

transactions = [
    {"id": 1, "amount": -200, "type": "withdraw"},
    {"id": 2, "amount": 1000, "type": "deposit"},
    {"id": 3, "amount": -500, "type": "withdraw"},
    {"id": 4, "amount": 200, "type": "deposit"}
]

def transation_generator(transactions):
    for transaction in transactions:
        yield transaction

gen = transation_generator(transactions)

print(next(gen))