numlist = []

while True:
    value = input("Enter the number: ")
    if value == "":
        break
    
    else:
        try:
            value = int(value)
            numlist.append(value)
        except ValueError:
            print("Please enter a valid numeric value.")
            continue

        

numlist.sort(reverse=True)
topfive = numlist[:5]

print("Five largest numbers:")
for number in topfive:
    print(number)
    