import random

capital_cities = {"Slovenia": "ljubljana", "Serbia": "belgrade",
                  "Croatia": "zagreb", "Germany": "berlin",
                  "Netherlands": "amsterdam", "Belgium": "brussels",
                  "Hungary": "budapest", "Ireland":  "dublin",
                  "Finland":  "helsinki", "Spain":  "madrid"}

print("Hello this is a simple geography quiz")

country = random.choice(list(capital_cities.keys()))
check = capital_cities.get(country)

while True:
    print("What is the capital city of " + country + " ? ")
    answer = input("")
    answer_1 = answer.lower()

    if answer_1 == check:
        print("Congratulations you are correct")
        break
    else:
        print("Sorry you are wrong please try again.")
