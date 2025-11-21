## Exercise 8: Simple Search - 30 Marks

#Creating a list of names
names = ["Jake","Zac", "Ian", "Ron", "Sam", "Dave"]
#Name we have to find
search = "Sam"
#Checking the name in the list
if search in names:
    print(f"{search} is there on the list")
else:
    print(f"{search} is not there in the list")