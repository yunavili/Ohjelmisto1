import random


def diceRoll():
    return random.randint(1, 6)
  

roll = 0

while roll != 6:
    roll = diceRoll()
    print(f"Rolled {roll}")

