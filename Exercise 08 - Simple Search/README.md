## Exercise 8: Simple Search - 30 Marks

names = ["Jake","Zac", "Ian", "Ron", "Sam", "Dave"]
search = input("Enter your name:")
if search in names:
    print(f"{search} is there on the list")
else:
    print(f"{search} is not there in the list")