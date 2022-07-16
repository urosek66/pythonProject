print("Hello this app is a simple unit converter.Here you can convert km in miles")

try_again = "Yes"

while try_again == "Yes":
    kilometer = int(input("Enter number of kilometers: "))
    miles = kilometer / 1.609344
    print(f"{kilometer} km is {miles} miles")

    try_again = (input("Do you want to continue(Type Yes): "))

print("Goodbye and see you soon")
