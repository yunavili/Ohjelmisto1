import random


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


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
