# Simple training with functions with some arguments
def make_sandwich(*args):
    return f"Sandwich with: {', '.join(args)}"

print(make_sandwich("tomato", "salat", "bread", "olive"))

def build_profile(first, last, **kwargs):
    kwargs["first_name"] = first
    kwargs["last_name"] = last
    return kwargs

my_profile = build_profile("dastan", "bolatkhan", location = 'almaty', field = 'math')

print(my_profile)

# Another way to work with kwargs
def make_car(brand, mark, **kwargs):
    return {"brand_name": brand, "mark_name": mark, **kwargs}

my_car = make_car("subaru", "outback", color = "red", type="mechanic")

print(my_car)



amount = float(input("Please enter your amount in USD: "))

def usd_to_kzt(amount, rate = 545):
    return amount * rate

print(f"Your {amount} USD In Kazakhstan tenge: {usd_to_kzt(amount)} KZT")

print(usd_to_kzt(amount))