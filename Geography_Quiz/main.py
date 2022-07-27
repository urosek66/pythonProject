import random

capital_cities = {"Slovenia": "Ljubljana", "Serbia": "Belgrade",
  "Croatia": "Zagreb", "Germany": "Berlin",
  "Netherlands":"Amsterdam", "Belgium": "Brussels",
  "Hungary": "Budapest", "Ireland":  "Dublin",
   "Finland":  "Helsinki", "Spain":  "Madrid"}

print("Hello this is a simple geography quiz")

country = random.choice(list(capital_cities.keys()))
check = capital_cities.get(country)

while True:
    print("What is the capital city of " + country + " ? ")
    answer = input("")

    if answer == check:
        print("Congratulations you are correct")
        break
    else:
        print("Sorry you are wrong please try again.")