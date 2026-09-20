import math

def calcSum(numbers):
    if not numbers:
        print("List is empty!")
        return []
        
    result = []

    for num in numbers:
        if num % 2 != 0:
            result.append(num)

    return (result)

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if isinstance(numList, list):
    print(f"The final look of the list is: {calcSum(numList)}")
else:
    print("Provided variable is not a list!")