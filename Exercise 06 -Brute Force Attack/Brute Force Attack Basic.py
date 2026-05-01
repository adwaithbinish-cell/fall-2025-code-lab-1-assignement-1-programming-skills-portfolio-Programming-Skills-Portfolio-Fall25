## Exercise 6: Brute Force Attack - 30 Marks

#Defining the correct password
password = "12345"

#Asking the user to input the password
while True:
    a = input("Enter your password:")

    if a == password:
        print("The password you entered is correct!")
        break
    else:
        print("Wrong password! Try again.")