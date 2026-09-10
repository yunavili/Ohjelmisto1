names = set()
print("Enter names (press Enter on empty line to stop): ")

while True:
    name = input("Enter name: ").strip()

    if name == "":
        break
    
    if name in names:
        print("Previously added name")
    else:
        print(f"{name} is a new name")
        names.add(name)

print("\nList of entered names:")
for name in names:
    print(name)