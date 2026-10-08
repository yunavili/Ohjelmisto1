Westerosi Traveler -Game

A text-based adventure game set in the world of Westeros.

Tekijä: Yuliia Ivanska eli yunaiv (mun nickname)

THE IDEA

Westerosi Traveler is a terminal role-playing game inspired by tabletop RPGs Dungeons & Dragons. "Winter is coming": the player is a traveler stranded in the harsh lands of Westeros, where danger lurks in every room. The game world consists of five rooms connected by a shadowy hallway. The player explores the rooms, collects items, talks to NPCs and fights White Walkers by rolling dice.

The game is played entirely through a numbered main menu: the player types the number of the action they want to perform, and the game responds with printed text. Exactly like in a very old-school text adventure!

THE GOAL

The player starts in the Hallway of the castle and find his goal there. There are three different endings:

1. Death – the player's HP drops to 0 in a fight.
2. A New Alliance – the player meets Jon Snow in the Guard post and chooses to leave Westeros together with him. Travelling was never meant to be a solo adventure.
3. The Survivor – the player defeats every enemy (the Night Walker in the Hallway and the White Walker in the Mystical vault) and survives against all odds.

There is no single "correct" way to finish the game – the player chooses whether to fight their way through, seek an alliance, or perish trying.

OPERATING PRINCIPLES

The game is written in Python using only the standard library. It is started from the 'peliprojekti' folder python main.py -file

At startup the game writes and displays the intro "intro.txt' and the instructions 'ohjeet.txt'. If a save file 'saves.json' exists, the player will load it, otherwise the game asks for the player's name and age, players under 12 are not allowed to play.

The heart of the game is a turn-based game loop src/game.py:

1. Check whether one of the three endings has been reached in src/endings.py.
2. Show the main menu.
3. Read the player's choice and run the corresponding action.
4. Repeat until an ending occurs or the player exits.

MODULES

'main.py' - Entry point: writes intro files, sets up the player, starts the game loop
'src/game.py' - Main menu, player setup and the game loop
'src/world.py' - Builds the whole game world: items, characters, rooms, enemies and dice
'src/characters.py' - 'Character' base class and the Player', 'Enemy' and 'NPC' subclasses 
'src/items.py' - 'Item', 'HealingPotion' and the 'Dice' class 
'src/rooms.py' - 'Room' class: items, enemies, NPCs, descriptions and interactions
'src/combat.py' - Turn-based fighting: attack, take damage, escape
'src/endings.py' - Checks the three end conditions of the game
'src/save_manager.py' - Saving and loading the game to/from 'saves.json' (JSON format)
'src/intro.py' - Intro and instruction texts shown at startup

KEY MECHANICS

- Dice rolls DND-style: the player's attack damage is a roll of a six-sided die 'Dice.roll', and the menu also offers a free d20 roll. The 'Dice' class supports any number of sides, multiple dice, modifiers and advantage/disadvantage rolls.
- Combat: in a fight the player chooses 'Attack' or 'Run' each turn. Enemies counterattack with a fixed attack power (Night Walker 5, White Walker 4). A defeated enemy is removed from its room. Dying no longer ends the whole game immediately – the ending check handles it on the next loop.
- Inventory with a weight limit: every item has a weight, and the player can carry at most 100 units. Items that are too heavy cannot be picked up, and thrown-away items are gone forever.
- Rooms and interactions: each room has a description and may hold an item, an enemy, an NPC and special interactions (for example "inspect shackles" or "touch runes").
- Saving: the game state (player, room, inventory, room items, enemy HP) is stored in a human-readable JSON file.

FUNCTIONALITIES

The main menu offers the following actions:

1. Roll a dice (d20)
2. Stats – name, age, HP and health status (Full Health / Injured / Critical / Dead)
3. Move – travel to any of the five rooms (Dungeon Cell, Ancient library, Mystical vault, Guard post, Hallway)
4. Rest – fully restore HP
5. Exit the game
6. Show inventory
7. Throw an item out (destroys it permanently and frees up weight)
8. Take the item lying in the current room
9. Check HP
10. Inspect the current room
11. Interact with the room e.g. search the table in the Guard post, which can lead to Ending 2
12. Save game
13. Load game
14. Fight the enemy in the current room

Additional details:

- Moving into a room with an enemy automatically offers a fight.
- The player can always 'Run' from a fight.
- Known limitation: the healing potion exists as an item, but using it is not yet connected to the menu – HP is currently restored only by resting.

SUSTAINABLE DEVELOPMENT

Sustainability has been taken into account in several ways:

Ecological: Runs on lightweight text without graphics or network needs, saving energy.
Social: age-gated at 12+, and offers peaceful win conditions without glorifying violence.
Economic: Zero license or maintenance costs due to having no external dependencies.
Technical: Modular structure, clear docstrings, and simple code.
Data Responsibility: Keeps player name, age, and progress strictly local in a standard json.