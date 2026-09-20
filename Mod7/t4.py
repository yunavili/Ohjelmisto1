import math

def calcSum(numbers):
    if not numbers:
        print("List is empty!")
        return 0
    
    return sum(numbers)

numList = [1, 2, 3, 4, 5]

if isinstance(numList, list):
    totalSum = calcSum(numList)
    print(f"The total sum of the list is: {totalSum}")
else:
    print("Provided variable is not a list!")