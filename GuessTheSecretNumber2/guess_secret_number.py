import functions

while True:
    selection = input("What would you like to do: A-play a game, B-Se top results or C-quit: ")

    if selection == "A":
        functions.play_game(level=input("Choose level of the game hard or easy : "))
    elif selection == "B":
        functions.get_best_score()
    else:
        print("Goodbye and see you soon")
        break
