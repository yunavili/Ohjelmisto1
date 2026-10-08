INTRO_TEXT = """    WESTEROSI TRAVELER

Winter is coming, traveler.
You find yourself in the harsh lands of Westeros,
where danger lurks at every corner. From the icy walls
of the North to the dusty roads of the Riverlands,
only the wisest and the strongest will win this game.
"""

INSTRUCTIONS_TEXT = """    GAME INSTRUCTIONS

1. Use the main menu numbers to perform actions or manipulate the game.
2. Inventory is not endless! Carrying too much will downgrade your ability to fight.
3. Don't forget to check on your health.
4. Travel through the places, collect items, have conversations with NPCs and fight white walkers!
5. There's 3 ways to finish the game. Play to find them out!
"""


def write_intro_files():
    """Write the intro and instructions text files and show them."""
    with open("intro.txt", "w") as file:
        file.write(INTRO_TEXT)

    print(INTRO_TEXT)

    with open("ohjeet.txt", "w") as file:
        file.write(INSTRUCTIONS_TEXT)

    print(INSTRUCTIONS_TEXT)
