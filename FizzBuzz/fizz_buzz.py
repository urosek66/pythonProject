number = int(input("Select a number between 1 and 100: "))
counter = 1

while counter <= number:

    if counter % 3 == 0 and counter % 5 == 0:
        print("fizzbuzz")
    elif counter % 3 == 0:
        print("fizz")
    elif counter % 5 == 0:
        print("buzz")
    else:
        print(counter)

    counter += 1



