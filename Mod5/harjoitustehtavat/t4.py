import random

print("""Write a game where the computer randomly selects an integer between 1-10. 
To close the program input 'Enter'""")

number = random.randint(1, 10)

while True:
    guess = input("Guess the number between 1 and 10: ")
    if guess == "":
            print("Bye!")
            break
        
    try:
        value = int(guess)
        if 0 > value or value > 10:
            print("You've gone beyond the numbers, try again!")

        elif value > number:
            print("Too high guess!")

        elif value < number:
            print("Too low guess heh")

        elif value == number:
            print(f"{value} is a right number, you won!")
            break
           
    except ValueError:
        print("Shameless scoundrel! Print a numeric value!")
