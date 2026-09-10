import math
import sys

print("This program checks whether the entered number is prime.")
uinput = input("Enter a number here: ")

if uinput == "":
    print("Okay bye.")
    sys.exit()

n = int(uinput)

if n <= 1:
    print(f"{n} is not a prime number")

elif n in (2, 3):
    print(f"{n} is a prime number")

else:
    for i in range(2, math.isqrt(n) + 1):
        remainder = n % i
        if remainder == 0:
            print(f"{n} is evenly divisible by {i}, so it is composite number")
            break

    else:
            print(f"{n} is not evenly divisible by {i}, so it is prime number")

    
