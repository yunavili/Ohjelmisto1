import random
import sys

print("This program will ask for a player's name and age.")
player_name = input("Tell us your name: ")
players_age = input("what's your age?: ")

while True:
    if int(players_age) < 12:
        print(f"You're {players_age} year's old, you're too young for this game!")
        sys.exit()
    else:
        print(f"Hello, {player_name}! You're {players_age} years old, that's a pretty solid age, but even so you'll prove yourself!")
        break

while True:
    print("""
        1. roll (d20) (Random action with varying degrees of success)
        2. stats
        3. act
        4. rest
        5. exit""")

    player_input = input("Select one action: ").strip()

    if player_input == "1":
        d20 = random.randint(1, 20)
        print(f"\nYou try to do something completely random... Roll: {d20}")

        if d20 == 1:
            print("Critical Fail! You tripped over your own cloak and accidentally slapped yourself in the face.")
        elif 2 <= d20 <= 5:
            print("Bad luck! You tried to strike a cool hero pose, but immediately stubbed your toe on a small rock.")
        elif 6 <= d20 <= 10:
            print("You attempted to tell a witty joke, but nobody laughed except a very confused crow.")
        elif 11 <= d20 <= 15:
            print("Success! You found a shiny coin in your pocket and successfully winked at a tavern guard.")
        elif 16 <= d20 <= 19:
            print("Great success! You successfully convinced a stray dog that you are its rightful king.")
        elif d20 == 20:
            print("Critical success! You hit a perfect backflip! The gods themselves applaud your useless talent!")

    elif player_input == "2":
        print("Your stats: Strength - 10, Dexterity - 10, HP - 10/10")

    elif player_input == "3":
        print("You performed an action!")

    elif player_input == "4":
        print("You rested and recovered your strength.")

    elif player_input == "5":
        print("Exiting game.")
        break

    else:
        print("Invalid choice, please try again.")
