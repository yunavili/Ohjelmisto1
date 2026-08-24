name = input("Enter your name: ")

filtered_name = ""

for char in name:
    if char.isalpha() or char == "-":
        filtered_name += char

#"".join(char for char in name if char.isalpha() or char == "-")

final_name = filtered_name.title().strip()

if final_name == "Batman":
    print("Oh wow Batman is here to save us!")
elif final_name == "Gandalf" or final_name == "gandalf":
    print("You shall not pass!")
elif final_name == "Anna-Maria" or final_name == "anna-maria":
    print(f"Hello, {final_name}, I love your name!")
elif final_name == "Aino" or final_name == "aino":
    print(f"Hello, {final_name}, here's a joke for you: Two knights meet at a tournament. One says to the other 'Hey, why is your armor creaking so strangely? And the other answers 'It's just the fiddler from the castle crawled in to warm up!'")
elif final_name:
    print(f"Hello, {final_name}!")
else:
    print("Please enter a valid name.")
