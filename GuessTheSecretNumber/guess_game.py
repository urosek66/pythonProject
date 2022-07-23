import random
import json
import datetime


secret = random.randint(1, 30)
attempts = 0
wrong_attempts = 0

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

sorted_list = sorted(score_list, key=lambda k: k["attempts"])[:3]

for best_score in sorted_list:
    print("Player: " + best_score["player_name"] + " had " + str(best_score["attempts"]) + " attempts, the number was "
          + str(best_score["number"]) + " date: " + best_score.get("date"))


name = input("Enter your name: ")

while True:
    guess = int(input("Guess the right number(between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"player_name": name, "attempts": attempts, "date": str(datetime.datetime.now()),
                           "number": secret, "wrong_guesses": wrong_attempts})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Congratulations you are correct the number is " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        wrong_attempts += 1
        print("You are  wrong ... try something smaller")
    elif guess < secret:
        wrong_attempts += 1
        print("You are wrong ... try something bigger")
