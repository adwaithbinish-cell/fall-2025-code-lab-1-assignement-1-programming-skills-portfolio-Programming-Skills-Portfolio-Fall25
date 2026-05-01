## Exercise 8: Simple Search - 30 Marks

#Creating a list of names
names = ["Jake","Zac", "Ian", "Ron", "Sam", "Dave"]

#Asking the user to search for a name
search = input("Enter your name: ")

#Checking the name the user entered in there on the list
for name in names:
    if name.lower() == search.lower():
        print("Sam is there on the list")
        break
else:
    print("Sam is not there in the list")