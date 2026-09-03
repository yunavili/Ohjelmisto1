while True:
    print(f"""This is calculator. Choose the operation and enter your 2 numbers
    1. Addition a + b
    2. Substraction a - b
    3. Multiply a * b
    4. Close the program""")


    operation = str(input("Choose the operation(1-4): "))

    if operation == "4":
       print("Goodbye!")
       break
    elif operation in ("1", "2", "3"):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

    if operation == "1":
        print(f"Result: {a + b:.2f}")
    elif operation == "2":
        print(f"Result: {a - b:.2f}")
    elif operation == "3":
       print(f"Result: {a * b:.2f}")
    else:
        print("Enter a valid value")





