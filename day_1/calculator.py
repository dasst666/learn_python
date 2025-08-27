valid_operators = {"+", "-", "*", "/"}
while True:
    print("Hello its a simple python calculator")

    num_1 = input("Please input first number: ")
    operator = input("Please inut operators like (+, -, *, /): ")
    num_2 = input("Please input second number: ")

    try:
        number_1 = float(num_1)
        number_2 = float(num_2)
    except ValueError:
        print("Please input only numbers")
        break
    
    if operator not in valid_operators:
        print("Plese input only valid operators like (+, -, *, /)")
        break

    def calculate_two(num_1, num_2, operator):
        if operator == "+":
            result = float(num_1) + float(num_2)
        elif operator == "-":
            result = float(num_1) - float(num_2)
        elif operator == "*":
            result = float(num_1) * float(num_2)
        elif operator == "/":
            result = float(num_1) / float(num_2)

        if result % result == 0:
            return int(result)
        else:
            return result

    def result(operator):
        return calculate_two(num_1, num_2, operator)

    print(f"The result is: {result(operator)}")