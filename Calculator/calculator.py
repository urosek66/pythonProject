first_number = int(input("Write first number: "))
second_number = int(input("Write second number: "))
operation = input("Add math operation here (you can choose beetwen +, -, *, /): ")

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)
else:
    print("I don't now this operation")
