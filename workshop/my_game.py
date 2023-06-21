# Rock/scissors/paper simple game that I created after 2 months of studying python at TU-Sofia.
# Player chooses rounds range and plays against PC. At the end the winner is displayed.

import random

user = input("Enter your name: ")

while True:
    try:
        rounds = int(input("Create round ratio: "))
    except ValueError:
        print("Please a number!")
        continue
    
    break

OPTIONS = ["R", "P", "S"]

ITEMS = {
    "R": "rock", 
    "P": "paper", 
    "S": "scissors",
}

while True:
    final = ""
    pc_wins_counter = 0
    user_wins_counter = 0
    
    while pc_wins_counter < rounds and user_wins_counter < rounds:
        user_choice = input("Choose: rock-> R, paper-> P, scissors-> S, quit game-> Q: ").upper()

        if user_choice != "R" and user_choice != "P" and user_choice != "S" and user_choice != "Q":
            print("Wrong user input!")
            continue

        if user_choice == "Q":
            print("Game over! Goodbye...")
            break
        
        pc_choice = random.choice(OPTIONS)
        
        print(f"{user}'s choice-> {ITEMS[user_choice]}; PC choice-> {ITEMS[pc_choice]}")
        
        if user_choice == pc_choice:
            final = "Equal"
        elif user_choice == "R" and pc_choice == "P":
            final = "PC wins"
        elif user_choice == "P" and pc_choice == "R":
            final = f"{user} wins"
        elif user_choice == "R" and pc_choice == "S":
            final = f"{user} wins"
        elif user_choice == "S" and pc_choice == "R":
            final = "PC wins"
        elif user_choice == "P" and pc_choice == "S":
            final = "PC wins"
        elif user_choice == "S" and pc_choice == "P":
            final = f"{user} wins"
        else:
            print("Unexpected error! Try again...")
            continue

        if final == "PC wins":
            pc_wins_counter += 1
        elif final == f"{user} wins":
            user_wins_counter += 1
        elif final == "Equal":
            pass

        print(final)
        print(f"{user}'s win counter = {user_wins_counter} / PC win counter = {pc_wins_counter}")


    if pc_wins_counter == rounds:
        print(f"PC wins!!! {pc_wins_counter} by {user_wins_counter}")
    elif user_wins_counter == rounds:
        print(f"{user} wins!!! {user_wins_counter} by {pc_wins_counter}")
        
    play_again = input("Do you want to play again(Yes/No): ").upper()
    while play_again != "YES" or play_again != "NO":
        if play_again == "YES":
            break
        elif play_again == "NO":
            print("Game over! Goodbye...")
            exit(0)
        else:
            print("Invalid command!")
            play_again = input("Do you want to play again(Yes/No): ").upper()