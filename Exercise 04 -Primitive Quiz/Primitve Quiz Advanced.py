## Exercise 4: Primitive Quiz - 30 Marks

#Dictionary of the European countries and their capitals
info = {
    "Belgium": "Brussels",
    "Spain": "Madrid",
    "Hungary": "Budapest",
    "United Kingdom": "London",
    "Italy": "Rome",
    "Portugal": "Lisbon",
    "France": "Paris",
    "Croatia": "Zagreb",
    "Poland": "Warsaw",
    "Germany": "Berlin"
}

marks = 0

#Asking the questions
for country in info:
    answer = input("What is the capital of " + country + "? ")
    if answer.lower() == info[country].lower():
        print("The answer you entered is correct!")
        marks += 1
    else:
        print("Wrong! The correct answer is " + info[country] + ".")
        
#Print final score
print(f"\nYou got {marks} out of {len(info)} correct!")