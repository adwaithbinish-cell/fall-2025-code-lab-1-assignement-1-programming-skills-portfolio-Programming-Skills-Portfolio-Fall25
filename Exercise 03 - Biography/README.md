## Exercise 3: Biography - 25 Marks

name = str(input("Enter your name:"))
hometown = str(input("Enter your hometown:"))
age = int(input("Enter your age:"))
personal_info={
    "Name":name,
    "Hometown":hometown,
    "Age":age}
print(f"Name: {personal_info['Name']} \nHometown: {personal_info['Hometown']} \nAge: {personal_info['Age']}")