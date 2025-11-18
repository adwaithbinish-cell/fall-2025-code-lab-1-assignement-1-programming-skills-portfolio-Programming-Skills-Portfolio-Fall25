## Exercise 4: Primitive Quiz - 30 Marks

info = {
    "Spain": "Madrid",
    "Egypt": "Cairo",
    "France": "Paris",
    "Germany": "Berlin",
    "India": "Delhi",
    "Italy": "Rome",
    "Portugal": "Lisbon",
    "China": "Beijing",
    "Belgium": "Brussels",
    "Japan": "Tokyo"
}

marks = 0

for country, capital in info.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.strip().lower() == capital.lower():
        print("The answer you entered is correct!")
        marks += 1
    else:
        print(f"Wrong! The correct answer is {capital}.")
print(f"\nYou got {marks} out of {len(info)} correct!")