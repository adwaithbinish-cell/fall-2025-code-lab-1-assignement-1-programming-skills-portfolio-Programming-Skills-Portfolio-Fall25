name = str(input("Enter your name:"))
hometown = str(input("Enter your hometown:"))
age = int(input("Enter your age:"))
Biography={
    "Name":name,
    "Hometown":hometown,
    "Age":age}
print(f"Name: {Biography['Name']} \nHometown: {Biography['Hometown']} \nAge: {Biography['Age']}")