"""Player setup, main menu and the game loop."""

import os
import sys
import textwrap

from src import world
from src.combat import fight
from src.endings import check_endings
from src.save_manager import load_game, save_game


def setup_player(player):
    """Load an existing save or ask for a new player's name and age."""
    loaded = False

    if os.path.exists("saves.json"):
        choice = input("Save file detected! Do you want to load save? (1. Yes / 2. No): ").strip()

        if choice in ["1", "Yes", "yes"]:
            loaded = load_game()

    if not loaded:
        # it's time to banish the demon (to refactor the character's sys)
        print("This program will ask for a player's name and age.")

        player_name = input("Tell us your name: ")
        player_age = input("what's your age?: ")

        if int(player_age) < 12:
            print(f"You're {player_age} year's old, you're too young for this game!")
            sys.exit()
        else:
            print(f"Hello, {player_name}! You're {player_age} years old, that's a pretty solid age, but even so you'll prove yourself!")

            player.name = player_name
            player.age = int(player_age)

    return player


def show_menu():
    print(textwrap.dedent("""
    1. Just roll a dice (d20)
    2. Stats
    3. Move
    4. Rest
    5. Exit
    6. Show inventory
    7. Throw item out
    8. Take item
    9. Check on your HP
    10. Inspect room
    11. Interact with room
    12. Save game
    13. Load game
    14. Fight
    """))


def roll_dice():
    world.dice_20.roll(1, 1)


def show_stats(player):
    print(
        f"Your stats:\n"
        f"Name: {player.name}\n"
        f"Age: {player.age}\n"
        f"HP: {player.player_hp}/{player.max_hp} ({player.get_hp_status()})\n"
        f"Strength: 10\n"
        f"Dexterity: 10"
    )


def move_player(player):
    rooms = world.rooms

    room_choice = input(
        "Where do you want to go?\n"
        "1. Dungeon Cell\n"
        "2. Old library\n"
        "3. Mystical vault\n"
        "4. Guard post\n"
        "5. Hallway\n"
    ).strip()

    try:
        choice_idx = int(room_choice)

        if 1 <= choice_idx <= len(rooms):

            selected_room = rooms[choice_idx - 1]

            if player.place == selected_room:
                print("You're already here!")

            else:
                player.move(selected_room)

                # ADDED:
                # If an enemy is in the room, automatically offer a fight.
                if selected_room.enemy is not None:
                    print(
                        f"\nThe {selected_room.enemy.name} blocks your path!"
                    )

                    fight_choice = input(
                        "Do you want to fight?\n"
                        "1. Yes\n"
                        "2. No\n"
                        "> "
                    ).strip()

                    if fight_choice == "1":
                        fight(player, selected_room.enemy)

        else:
            print("There's no such room!")

    except ValueError:
        print("Please enter a valid room number!")


def rest_player(player):
    player.player_hp = player.max_hp

    print(
        f"You rested and fully recovered your health! "
        f"({player.player_hp}/{player.max_hp} HP)"
    )


def throw_item_out(player):
    player.show_inventory()

    try:
        player_throw = int(
            input("Which item you want to throw out? (a number): ")
        ) - 1

        player.throw_item(player_throw)

    except ValueError:
        print("Please enter a valid number!")


def check_hp(player):
    print(
        f"Current HP: {player.player_hp}/{player.max_hp} "
        f"| Status: {player.get_hp_status()}"
    )


def interact_with_room(player):
    if not player.place.interactions:
        print("There is nothing to interact with here.")

    else:
        player.place.show_interactions()

        try:
            interaction_choice = int(
                input("Choose an interaction: ")
            ) - 1

            interactions = list(player.place.interactions.keys())

            if 0 <= interaction_choice < len(interactions):

                selected_action = interactions[interaction_choice]

                player.place.interact(selected_action)

                # Special NPC ending interaction
                if player.place == world.room4:
                    print("\nJon Snow looks at you.")

                    npc_choice = input(
                        "Do you want to leave Westeros with him?\n"
                        "1. Yes\n"
                        "2. No\n"
                        "> "
                    ).strip()

                    if npc_choice == "1":
                        player.met_npc = True

            else:
                print("Invalid interaction.")

        except ValueError:
            print("Please enter a valid number.")


def fight_enemy(player):
    if player.place.enemy is None:
        print("There is no enemy here.")

    elif player.place.enemy.player_hp <= 0:
        print("There is no living enemy here.")

    else:
        fight(player, player.place.enemy)


def handle_action(player, player_input):
    """Run one menu action. Returns False when the game should stop."""
    if player_input == "1":

        roll_dice()

    elif player_input == "2":

        show_stats(player)

    elif player_input == "3":

        move_player(player)

    elif player_input == "4":

        rest_player(player)

    elif player_input == "5":

        print("Exiting game. Farewell, adventurer!")
        return False

    elif player_input == "6":

        player.show_inventory()

    elif player_input == "7":

        throw_item_out(player)

    elif player_input == "8":

        player.collect_item()

    elif player_input == "9":

        check_hp(player)

    elif player_input == "10":

        player.place.inspect()

    # ADDED:
    elif player_input == "11":

        interact_with_room(player)

    elif player_input == "12":

        save_game()

    elif player_input == "13":

        load_game()

    # ADDED:
    elif player_input == "14":

        fight_enemy(player)

    else:

        print("Invalid choice, please try again.")

    return True


def run_game(player):
    try:
        while True:

            if check_endings(player):
                break

            show_menu()

            player_input = input("Select one action: ").strip()

            if not handle_action(player, player_input):
                break

    except KeyboardInterrupt:

        print("\nGame closed. See you next time!")


# сделать взаимодействие с комнатами
# гг атакует кубиком
# написать саму игру и концовки (1 смерть, 2 концовка с нпс, 3 победа всех врагов)
