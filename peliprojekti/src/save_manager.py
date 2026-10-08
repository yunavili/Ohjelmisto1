import json
import os

from src import world


def load_game(filename="saves.json"):
    if not os.path.exists(filename):
        print("Save file does not exist.")
        return False
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        player = world.player
        rooms = world.rooms
        all_items = world.all_items
        enemies = world.enemies

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
    player = world.player
    rooms = world.rooms
    enemies = world.enemies

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
