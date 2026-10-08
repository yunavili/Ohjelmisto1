"""Game world: items, characters, rooms and the player."""

from src.characters import Enemy, NPC, Player
from src.items import Dice, HealingPotion, Item
from src.rooms import Room

# items that get duplicated??? limit it to 5 heals? No. Let it be infinite. That's what I want for myself.

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


enemies = [
    white_walker,
    night_walker
]
