# Gets the class 'Pirate' (all classes in file), from the file Pirate.
from Pirate import *
# Import library
import random 




# My pirate objects
pirateDummy = Pirate("Dummy") # Instanziate a new object from Pirate class. 
pirateOne = Pirate("Jack")
pirateTwo = Pirate("Scratch")
pirateThree = Pirate("Bill")
pirateFour = Pirate("Hook")
pirateFive = Pirate("Rip")




# My pirate list
listOfPirates = [pirateDummy, pirateOne, pirateTwo, pirateThree, pirateFour, pirateFive] # List. 
listLength = len(listOfPirates) # Return the number of pirates in the list.




# Functions: 
def resetPointers() :
    
    i = 0 # Pointer is set to zero

    # Uses a for loop.. 
    for pirates in listOfPirates :
        # to set the pointer for each pirate in the circle
        if i < listLength - 1 :
            listOfPirates[i].setPointer(listOfPirates[i+1]._name)
            i = i + 1
        elif i == listLength - 1 :
            listOfPirates[i].setPointer(listOfPirates[0]._name)
            if listOfPirates[i]._name == listOfPirates[0]._name :
                print("You are the last pirate in the circle. Congratulations,", listOfPirates[i]._name, "you won!")
                print()
                exit()
        #else :
            #print("Can I get some rum?")


# Function: Creates the circle of pirates that points to eachother 
def showPointers() :
    
    x = 0 # Pointer is set to zero 

    # Uses a for loop to create the circle..
    for pirates in listOfPirates :
        # sets the pirate to point to the following pirate in the circle etc. 
        if x <= listLength :
            print ("This pirate is called", listOfPirates[x].getName(), "and he points to pirate", listOfPirates[x].getPointer())
            x = x + 1 # adds 1 to pointer for each pirates in the list.
        #else :
            #print("Can I get some kebab?")




# Setting up Pirates
resetPointers() # Calls the function.
print("There are", len(listOfPirates), "pirates in the game.") # Prints how many pirates there is in the game. 
print()

showPointers() # Call the function.
print()




# Setting up the Game
while listLength > 2 :
    count = 8 # Counting number.
    i = 0

    while i < count : 
        pirateJump = random.choice(listOfPirates) # Chooses the initial pirate (starting point).
        i = i + 1

        index = listOfPirates.index(pirateJump) # Saves the value of the pirates pointer, who should walk the plank.
        print()

        # Prints a message.
        print("The pirate who must walk the plank is number", index, "who is", listOfPirates[index]._name)
        print()
        listOfPirates.pop(index) # Removes the pirate from the list.

        listLength = len(listOfPirates) # Counts the list again.
        print("There are now", len(listOfPirates), "pirates left in the game.") # Prints a message containing the number of pirates, who is left.
        print()

        resetPointers() # Calls the function.
        showPointers() # Calls the function.

  