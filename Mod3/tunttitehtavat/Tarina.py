name = input("Come up with a name for a character: ")
regret = input("What is a regret you would like to see in the story? ")


tarina1 = f"{name} stole the golden carrot, unlocked 100% of his brainpower, and immediately started a wildly successful crypto scam. He now lives in a bulletproof burrow, endlessly suffering from severe {regret}."
tarina2 = f"{name} slammed five pints of dwarven ale, slammed his fist on the bar, and challenged the local dragon to an arm-wrestling match. He lost both his arm and his dignity, leading to a lifetime of profound {regret}."
tarina3 = f"King {name} taxed breathing, banned weekends, and replaced the royal guards with very aggressive geese. The peasants revolted in five minutes, leaving the ousted monarch stranded in a swamp with nothing but eternal {regret}."

print("Choose a story:")
print("1. The Golden Carrot")
print("2. The Dwarven Ale")
print("3. The Taxed Breathing")

choice = input("Input the number of the story you want to for your character: ")
if choice == "1":
    print(tarina1)
elif choice == "2":
    print(tarina2)
elif choice == "3":
    print(tarina3)
else:
    print("Invalid choice. Please select 1, 2 or 3.")
