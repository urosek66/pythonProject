secret = 9
guess = int(input("Guess the right number(beetween 0 and 100): "))

if secret == guess:
    print("Congratulations you are correct the number is " + str(guess))
else:
    print("Sorry you are wrong try again")