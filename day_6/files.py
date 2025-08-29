while True:
    first_name = input("Please write your name here: ")

    if first_name == "q":
        break
 
    with open("numbers.txt", "a") as f:
        f.write(f"Hello {first_name}!\n")

