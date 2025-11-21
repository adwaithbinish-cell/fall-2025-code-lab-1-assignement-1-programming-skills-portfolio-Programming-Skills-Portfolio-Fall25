## Exercise 6: Brute Force Attack - 30 Marks

#Defining the correct password
password = 12345
#Asking the user to input the password
a = int(input("Enter your password:"))
while a != password:
    print("Wrong password! Try again.")
    a = int(input("Enter your password:"))
print("The password you entered is correct!")