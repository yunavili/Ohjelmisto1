print("This program prompts for a username and password until correct credentials are provided.")

username = "python"
password = "rules"

attempt = 0

while True:

    inpUn = str(input("Enter username: "))
    inpPass = str(input("Enter password: "))

    if inpUn == username or inpPass == password:
        print("Access granted")
        break
        
    else:
        attempt += 1 
        if attempt == 5:
            print("Access denied")
            break
        print("Wrong login or password")
        