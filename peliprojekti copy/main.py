import random
import sys
import textwrap
import json
import os

with open("intro.txt", "w") as file:
  text = """    WESTEROSI TRAVELER

Winter is coming, traveler.
You find yourself in the harsh lands of Westeros,
where danger lurks at every corner. From the icy walls
of the North to the dusty roads of the Riverlands,
only the wisest and the strongest will win this game
"""
  intro = file.write(text)
  print(text)

with open("ohjeet.txt", "w") as file:
  text = """    GAME INSTRUCTIONS

1. Use the main menu numbers to perform actions or manipulate the game.
2. Inventory is not endless! Carrying too much will downgrade your ability to fight.
3. Don't forget to check on your health.
4. Travel through the places, collect items, have conversations with NPCs and fight white walkers! 
5. There's 3 ways to finish the game. Play to find them out!
"""
  print(text)


class Character:
    def __init__(self, name, place, hp):
        self.name = name
        self.player_hp = hp
        self.max_hp = hp
        self.place = place

    def get_hp_status(self):
        if self.player_hp <= 0:
            return "Dead"
        elif self.player_hp < 10:
            return "Critical"
        elif self.player_hp < self.max_hp:
            return "Injured"
        else:
            return "Full Health"

    def getting_damage(self, damage):
        self.player_hp -= damage
        print(f"{self.name} took {damage} damage!")

        # Character no longer ends the whole game when HP reaches 0. Dying is not in trends these days.
        # Same works for enemies
        if self.player_hp <= 0:
            self.player_hp = 0
            return True

        return False


class Player(Character):

    def __init__(self, name, place, hp=20, max_weight=100):
        super().__init__(name, place, hp)
        self.inventory = []
        self.current_weight = 0
        self.max_weight = max_weight
        self.age = 0
        self.met_npc = False
    
    def move(self, room):
        self.place = room
        print(f"You have moved to the {room.name}.")

        if room.item is not None:
            print(f"{self.place.item.name.capitalize()} is shining in the room.")
        else:
            print("The room is that empty so the wind only disturbs you.")

        if room.enemy is not None:
            print(f"{room.enemy.name} Oh no, is here!")

        if room.characters:
            for character in room.characters:
                print(f"{character.name} is in the room.")

    def collect_item(self):
        item = self.place.item_granting()
        if item:
            if self.max_weight < self.current_weight + item.weight:
                print(f"You cannot pick up {item.name}, it's too heavy! Current weight: {self.current_weight}/{self.max_weight}")
            else:
                self.current_weight += item.weight
                self.inventory.append(item)
                print(f"{item.name.capitalize()} was added. Current weight: {self.current_weight}/{self.max_weight}")
        else:
            print("There's nothing to pick up")

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory:")
            for index, item in enumerate(self.inventory, start=1):
                print(f"{index}. {item.name.capitalize()}")

    def throw_item(self, index):
        if 0 <= index < len(self.inventory):
            item = self.inventory[index]
            self.inventory.remove(item)
            self.current_weight -= item.weight
            print(f"You threw away {item.name}. Now it's destroyed. Forever. \nCurrent weight: {self.current_weight}/{self.max_weight}")
        else:
            print("Item not in inventory")  # The issue is that will user delete by name or by button—or delete based on the index and a button press? By button i suppose

    def healing(self, potion):
        if self.player_hp >= self.max_hp:
            print("You are already at full health!")
        else:
            self.player_hp = min(self.player_hp + potion.hp_amount, self.max_hp)
            print(f"You used a healing potion and restored {potion.hp_amount} HP! Current HP {self.player_hp}/{self.max_hp}")

    #new
    def attack(self, enemy):
        damage = dice_6.roll()

        print(f"You attack {enemy.name} and deal {damage} damage!")

        enemy.getting_damage(damage)


class Enemy(Character):
    def __init__(self, name, hp, attack, place, loot=None):
        super().__init__(name, place, hp)
        self.attack_power = attack
        self.loot = loot

    def attack(self, target_player):
        print(f"{self.name} attacks {target_player.name} for {self.attack_power} damage!")
        target_player.getting_damage(self.attack_power)


class NPC(Character):
    def __init__(self, name, place, dialigue):
        super().__init__(name, place, hp=10)
        self.dialigue = dialigue

    def talk(self):
        print(f'{self.name}: "{self.dialigue}"')


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Room:
    def __init__(self, name, item=None, enemy=None, characters=None, description="Nothing special here.", interactions=None):
        self.name = name
        self.item = item
        self.enemy = enemy
        self.characters = characters or []
        self.description = description
        self.interactions = interactions or {}

    def item_granting(self):
        if not self.item:
            print("There is no item here to take.")
            return None

        granting_choice = input(f"Do you want to collect {self.item.name}?\n1. Yes\n2. No\n> ").strip().capitalize()
        if granting_choice in ["1", "Yes"]:
            picked_item = self.item
            self.item = None
            return picked_item
        else:
            print("You chose not to pick up the item.")
            return None

    def inspect(self):
        print(self.description)
    
    def interact(self, action):
        if action in self.interactions:
            print(self.interactions[action])
        else:
            print("The silence in the room just got significantly more awkward.")

    # ADDED:
    def show_interactions(self):
        if not self.interactions:
            print("There is nothing interesting to interact with here.")
            return

        print("Available interactions:")

        for index, action in enumerate(self.interactions, start=1):
            print(f"{index}. {action}")


class HealingPotion(Item):
    def __init__(self, name, weight, hp_amount):
        self.hp_amount = hp_amount
        super().__init__(name, weight)
        

class Dice:
    def __init__(self, sides=20):
        self.sides = sides
    
    def roll(self, count=1, modifier=0, mode=None):
        if mode == "adv" or mode == "dis":
            roll1 = random.randint(1, self.sides)
            roll2 = random.randint(1, self.sides)

            if mode == "adv":
                selected_roll = max(roll1, roll2)
            else:
                selected_roll = min(roll1, roll2)

            total = selected_roll + modifier
            return total
            
        roll_results = []
        for _ in range(count):
            roll = random.randint(1, self.sides)
            roll_results.append(roll)
        total = sum(roll_results) + modifier
        print(f"Rolled {count}d{self.sides}: {roll_results} (+{modifier}) = {total}")

        return total


# items that get duplicated??? limit it to 5 heals? No. Let it be infinite. That’s what I want for myself.

book = Item("Book of Inept Spells", 20)
dagger = Item("Rusty Dagger", 15)
stone = Item("Mysterious Glowing Stone", 35)
key = Item("Heavy Iron Key", 10)
healingPotion = HealingPotion("Healing potion", 5, 5)  # do not have use for now

all_items = [book, dagger, stone, key, healingPotion]


# ADDED:
# Enemies and NPCs are created before the rooms,
# but their place can be assigned afterwards.

white_walker = Enemy(
    "White Walker",
    hp=15,
    attack=4,
    place=None
)

night_walker = Enemy(
    "Night Walker",
    hp=18,
    attack=5,
    place=None
)

jon = NPC(
    "Jon Snow",
    place=None,
    dialigue="You don't have to fight them alone. There may still be a way out."
)


room1 = Room(
    "Dungeon Cell", 
    item=dagger, 
    description="A cold, damp stone cell. Moisture drips from the ceiling.",
    interactions={
        "inspect shackles": "The iron shackles are rusted, but still firmly anchored to the wall."
    }
)

room2 = Room(
    "Ancient library", 
    item=book, 
    description="Dusty bookshelves line the walls, full of forgotten knowledge."
)

room3 = Room(
    "Mystical vault",
    item=stone,
    enemy=white_walker,
    description="Glowing runes flicker along the marble walls in this eerie vault.",
    interactions={
        "touch runes": "A mild shock runs up your arm! (Damage prevented)"  # but i'll add it later
    }
)

room4 = Room(
    "Guard post",
    item=key,
    characters=[jon],
    description="An abandoned guard post with a overturned wooden table.",
    interactions={
        "search table": "You search the overturned table but find nothing useful."
    }
)

start_location = Room(
    "Hallway",
    item=None,
    description="A long, shadowy corridor connecting multiple rooms."
)


# ADDED:
# Another enemy in the hallway.
night_walker.place = start_location
start_location.enemy = night_walker

white_walker.place = room3
jon.place = room4


rooms = [room1, room2, room3, room4, start_location]

# if there's something in the room game will notify about it
# if there's interactions to the room game will notify about it

dice_20 = Dice(20)
dice_6 = Dice(6)
dice_8 = Dice(8)
dice = Dice(12)
dice_4 = Dice(4)
dice_100 = Dice(100)

player = Player("", place=start_location)


# ADDED:
def fight(player, enemy):
    print(f"\nA fight begins against {enemy.name}!")

    while player.player_hp > 0 and enemy.player_hp > 0:

        print(f"\nYour HP: {player.player_hp}/{player.max_hp}")
        print(f"{enemy.name} HP: {enemy.player_hp}/{enemy.max_hp}")

        print("\n1. Attack")
        print("2. Run")

        choice = input("> ").strip()

        if choice == "1":

            player.attack(enemy)

            if enemy.player_hp <= 0:
                print(f"\nYou defeated the {enemy.name}!")

                # If enemy has loot, put it into the room.
                if enemy.loot is not None:
                    enemy.place.item = enemy.loot
                    print(f"{enemy.name} dropped {enemy.loot.name}!")

                enemy.place.enemy = None

                return True

            enemy.attack(player)

            if player.player_hp <= 0:
                print("\nYour body has officially given up on you. Game Over!")
                return False

        elif choice == "2":
            print("You escaped from the fight!")
            return False

        else:
            print("Invalid choice, please try again.")

    return False


# ADDED:
def check_endings(player):
    # Ending 1: player dies
    if player.player_hp <= 0:
        print("\nENDING 1: DEATH")
        print("Westeros has claimed another traveler.")
        return True

    # Ending 2: player meets NPC and chooses to leave with them
    if player.met_npc:
        print("\nENDING 2: A NEW ALLIANCE")
        print("You leave Westeros together with Jon Snow.")
        print("Perhaps survival was never meant to be a solo adventure.")
        return True

    # Ending 3: all enemies have been defeated
    all_enemies_defeated = True

    for enemy in enemies:
        if enemy.player_hp > 0:
            all_enemies_defeated = False

    if all_enemies_defeated:
        print("\nENDING 3: THE SURVIVOR")
        print("You defeated every enemy standing in your way.")
        print("Against all odds, you survived Westeros.")
        return True

    return False


# ADDED:
enemies = [
    white_walker,
    night_walker
]


def load_game(filename="saves.json"):
    if not os.path.exists(filename):
        print("Save file does not exist.")
        return False
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        player.name = data.get("player_name", "Unknown")
        player.age = data.get("player_age", 12)
        player.player_hp = data["player_hp"]

        # ADDED:
        player.met_npc = data.get("met_npc", False)

        for room in rooms:
            if room.name == data["place"]:
                player.place = room
                break

        player.inventory = []

        for itemname in data["inventory"]:
            for item in all_items:
                if item.name == itemname:
                    player.inventory.append(item)
                    break

        player.current_weight = data["current_weight"]

        for room in rooms:
            item_name = data["rooms_items"].get(room.name)

            if item_name:
                for item in all_items:
                    if item.name == item_name:
                        room.item = item
                        break
            else:
                room.item = None

        # ADDED:
        # Restore enemy HP.
        enemy_data = data.get("enemies", {})

        for enemy in enemies:
            if enemy.name in enemy_data:
                enemy.player_hp = enemy_data[enemy.name]["hp"]

        print(f"Save loaded successfully. Welcome back, {player.name}!")
        return True

    except FileNotFoundError:
        print("Error occurred while loading file.")
        return False


def save_game(filename="saves.json"):
    data = {
        "player_name": player.name,
        "player_age": player.age,
        "player_hp": player.player_hp,
        "place": player.place.name, 
        "inventory": [item.name for item in player.inventory],
        "current_weight": player.current_weight,

        # ADDED:
        "met_npc": player.met_npc,

        "rooms_items": {
            room.name: (room.item.name if room.item else None)
            for room in rooms
        },

        # ADDED:
        "enemies": {
            enemy.name: {
                "hp": enemy.player_hp
            }
            for enemy in enemies
        }
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Progress saved.")


# Загрузка сохранения или новый ввод имени/возраста
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


try:
    while True:

        if check_endings(player):
            break

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

        player_input = input("Select one action: ").strip()

        if player_input == "1":

            dice_20.roll(1, 1)

        elif player_input == "2":

            print(
                f"Your stats:\n"
                f"Name: {player.name}\n"
                f"Age: {player.age}\n"
                f"HP: {player.player_hp}/{player.max_hp} ({player.get_hp_status()})\n"
                f"Strength: 10\n"
                f"Dexterity: 10"
            )

        elif player_input == "3":

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

        elif player_input == "4":

            player.player_hp = player.max_hp

            print(
                f"You rested and fully recovered your health! "
                f"({player.player_hp}/{player.max_hp} HP)"
            )

        elif player_input == "5":

            print("Exiting game. Farewell, adventurer!")
            break
        
        elif player_input == "6":

            player.show_inventory()

        elif player_input == "7":

            player.show_inventory()

            try:
                player_throw = int(
                    input("Which item you want to throw out? (a number): ")
                ) - 1

                player.throw_item(player_throw)

            except ValueError:
                print("Please enter a valid number!")

        elif player_input == "8":

            player.collect_item()

        elif player_input == "9":

            print(
                f"Current HP: {player.player_hp}/{player.max_hp} "
                f"| Status: {player.get_hp_status()}"
            )

        elif player_input == "10":

            player.place.inspect()

        # ADDED:
        elif player_input == "11":

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
                        if player.place == room4:
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

        elif player_input == "12":

            save_game()

        elif player_input == "13":

            load_game()

        # ADDED:
        elif player_input == "14":

            if player.place.enemy is None:
                print("There is no enemy here.")

            elif player.place.enemy.player_hp <= 0:
                print("There is no living enemy here.")

            else:
                fight(player, player.place.enemy)

        else:

            print("Invalid choice, please try again.")


except KeyboardInterrupt:

    print("\nGame closed. See you next time!")


# сделать взаимодействие с комнатами
# гг атакует кубиком
# написать саму игру и концовки (1 смерть, 2 концовка с нпс, 3 победа всех врагов)
