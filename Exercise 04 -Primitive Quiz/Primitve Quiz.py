## Exercise 4: Primitive Quiz - 30 Marks

#Dictionary of the European countries and their capitals
info = {
    "Spain": "Madrid",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Hungary": "Budapest",
    "Italy": "Rome",
    "Portugal": "Lisbon",
    "Croatia": "Zagreb",
    "Belgium": "Brussels",
    "Austria": "Vienna"
}
marks = 0
#Asking the questions
for country, capital in info.items():
    answer = input(f"What is the capital of {country}? ")
    #Ignoring capitalization
    if answer.strip().lower() == capital.lower():
        print("The answer you entered is correct!")
        marks += 1
    else:
        print(f"Wrong! The correct answer is {capital}.")
#Print final score
print(f"\nYou got {marks} out of {len(info)} correct!")