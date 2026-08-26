import random

print("This program creates and prints two different combination lock codes:")

digit_3 = "".join(str(random.randint(0, 9)) for i in range(3))
digit_4 = "".join(str(random.randint(0, 6)) for i in range(4))

print(f"3-digit combination is {digit_3}")
print(f"3-digit combination is {digit_4}")


