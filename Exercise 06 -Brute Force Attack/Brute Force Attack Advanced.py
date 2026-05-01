## Exercise 6: Brute Force Attack - 30 Marks

#Defining the correct password
password = "12345"

#Maximum number of attempts
attempts = 5

#Using while loop to control the attempts
while attempts > 0:
    a = input("Enter your password:")

    if a == password:
        print("The password you entered is correct!")
        break
    else:
        attempts -= 1
        print(f"Wrong password! You have {attempts} attempts left.")
    
if attempts == 0:
    print("You have used all your attempts! Access denied.")