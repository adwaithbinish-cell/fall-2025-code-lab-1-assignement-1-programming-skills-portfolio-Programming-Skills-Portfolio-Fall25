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

month = int(input("Enter your month:"))

if 1 <= month <= 12:
    if month == 2:
        leap = input("Is it a leap year?:")
        if leap == "yes":
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    else:
        print(f"Month {month} has {days_in_month[month]} days.")
else:
    print("This month number doesn't exist.")