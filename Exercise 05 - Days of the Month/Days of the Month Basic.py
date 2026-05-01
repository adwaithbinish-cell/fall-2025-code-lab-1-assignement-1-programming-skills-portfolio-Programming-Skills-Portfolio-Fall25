## Exercise 5: Days of the Month - 30 Marks

#Creating dictionary with the months and days
days_in_month = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31}

#Asking the user to input the month number
month = int(input("Enter your month:"))

#Checking if the month is valid
if month in days_in_month:
    print(f"Month {month} has {days_in_month[month]} days.")
else:
    print("This month number doesn't exist.")