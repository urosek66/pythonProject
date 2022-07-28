import random
import json
import datetime


def play_game(level):
    secret = random.randint(1, 30)
    attempts = 0
    wrong_attempts = []
    score_list = get_score_list()

    name = input("Enter your name: ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"player_name": name, "attempts": attempts, "date": str(datetime.datetime.now()),
                               "number": secret, "wrong_guesses": wrong_attempts, "game_level": level})

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break

        elif guess != secret:
            if level == "easy":
                if guess > secret:
                    wrong_attempts.append(guess)
                    print("Your guess is not correct... try something smaller")
                elif guess < secret:
                    wrong_attempts.append(guess)
                    print("Your guess is not correct... try something bigger")
            elif level == "hard":

                if guess > secret:
                    wrong_attempts.append(guess)
                    print("You are wrong try again")
                elif guess < secret:
                    wrong_attempts.append(guess)
                    print("Your are wrong try again")


def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())

        return score_list


def get_best_score():
    print("Best score results: ")
    score_list = get_score_list()
    sorted_list = sorted(score_list, key=lambda k: k["attempts"])[:5]

    for best_score in sorted_list:
        print("Player: " + best_score["player_name"] + " had " +
              str(best_score["attempts"]) + " attempts, the number was "
              + str(best_score["number"]) + " date: " + best_score.get("date") + " game level: " +
              str(best_score["game_level"]))

    return sorted_list
