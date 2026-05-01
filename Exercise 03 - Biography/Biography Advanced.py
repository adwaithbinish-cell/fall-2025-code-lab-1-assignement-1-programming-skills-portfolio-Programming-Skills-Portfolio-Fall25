## Exercise 3: Biography - 25 Marks

#Making the user input the details
name = str(input("Enter your name:"))
hometown = str(input("Enter your hometown:"))

#Checking if the age given is the string or integer
age = input("Enter your age:")
while not age.isdigit():
    print("Please enter a valid number.")
    age = input("Enter your age:")
age = int(age)

#Storing the information in a dictionary
Biography={
    "Name":name,
    "Hometown":hometown,
    "Age":age}

#Print the values
print(f"Name: {Biography['Name']} \nHometown: {Biography['Hometown']} \nAge: {Biography['Age']}")