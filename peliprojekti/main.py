import random
import sys

print("This program will ask for a player's name and age.")
player_name = input("Tell us your name: ")
players_age = input("what's your age?: ")

player_hp = 20
max_hp = 20

def get_hp_status(hp):
    if hp >= max_hp:
        return "Full Health"
    elif hp > 10:
        return "Injured"
    elif hp > 0:
        return "Critical"
    else:
        return "Dead"


inventory = ["Stale bread with an ancient mycelium demon", "An Esoteric Codex on Dried Toad Lore"]

def inventoryAdd(item):
    inventory.append(item)
    print(f"You've got: {item}")

def inventoryShow():
    for item in inventory:
            print(item)

def healing():
    global player_hp
    if player_hp >= max_hp:
        print("You are already at full health!")
        return
    
    player_hp = min(player_hp + 5, max_hp) 
    print(f"You ate a piece of bread and restored 5 HP! Current HP {player_hp}/{max_hp}")

def damaging():
    global player_hp
    player_hp -= 5
    print("You ate a piece of moldy bread and lost 5 HP. It tasted as bad as it looked.")
    
    if player_hp <= 0:
        print("\nYou have perished from food poisoning... Game Over!")
        sys.exit()

def roll_d20():
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
    else:
        print("Critical success! You hit a perfect backflip! The gods themselves applaud your useless talent!")



if int(players_age) < 12:
    print(f"You're {players_age} year's old, you're too young for this game!")
    sys.exit()
else:
    print(f"Hello, {player_name}! You're {players_age} years old, that's a pretty solid age, but even so you'll prove yourself!")

try:
    while True:
        print("""
        1. Roll (d20)
        2. Stats
        3. Act
        4. Rest
        5. Exit
        6. Open inventory
        7. Add an item to inventory
        8. Check on your HP
        9. Eat some bread 
        10. Eat a piece of moldy bread
        """)

        player_input = input("Select one action: ").strip()

        if player_input == "1":
            roll_d20()

        elif player_input == "2":
            print(f"Your stats: HP: {player_hp}/{max_hp} ({get_hp_status(player_hp)}), Strength - 10, Dexterity - 10")

        elif player_input == "3":
            print("You performed an action!")

        elif player_input == "4":
            player_hp = max_hp
            print(f"You rested and fully recovered your health! ({player_hp}/{max_hp} HP)")

        elif player_input == "5":
            print("Exiting game. Farewell, adventurer!")
            break

        elif player_input == "6":
            inventoryShow()

        elif player_input == "7":
            newItem = input("What else do you want to put in your inventory?: ").capitalize().strip()
            if newItem:
                inventoryAdd(newItem)

        elif player_input == "8":
            status = get_hp_status(player_hp)
            print(f"Current HP: {player_hp}/{max_hp} | Status: {status}")

        elif player_input == "9":
            healing()

        elif player_input == "10":
            damaging()

        else:
            print("Invalid choice, please try again.")

except KeyboardInterrupt:
    print("\nGame closed. See you next time!")
