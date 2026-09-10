import random

dices = int(input("Enter the number of dices (6 faces): "))

totalsum = 0

for i in range(dices):
    dice = random.randint(1, 6)
    totalsum += dice
    print(totalsum)

print(f"The sum of dices is {totalsum}")

#OR

dices = int(input("Enter the number of dices (6 faces): "))
totalsum = sum(random.randint(1, 6) for i in range(dices))
print(f"The sum of dices is {totalsum}")