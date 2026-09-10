import random

print("You enter the number of sides your dice has, and then watch the program roll it over and over until you finally hit the highest number possible!")

def diceRoll(sides):
    return random.randint(1, sides)

usides = int(input("How many sides will be on the dice?: "))

roll = 0

while roll != usides:
    roll = diceRoll(usides)
    print(f"Rolled {roll}")