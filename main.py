# main.py

import os

clear = lambda: os.system('cls')

def printSet(name, set):
    print(f"{name}:")
    for id, term, definition in set:
        print(f"({id})\t{term}:\t{definition}")
    input("Press Enter to continue...")

def createSet():
    choice = True
    counter = 1
    set = []

    setName = input("Enter the name for your set: ")
    while choice == True:
        term = input(f"{counter} - Enter your term: ")
        definition = input("Enter your definition: ")
        cont = input("Would you like to add another term? (y/n): ")
        print(cont) # DEBUGGING
        if cont == "y":
            choice = True
        elif cont == "n":
            choice = False
        set.append([counter, term, definition])
        counter += 1
        clear()

    printSet(setName, set)
    

def reviewSet():
    print(0)

def editSet():
    print(0)

def deleteSet():
    print(0)

def getChoice():
    while True:
        try:
            choice = int(input("Enter a choice: "))
        except ValueError:
            print("Invalid choice.")
            continue
        if choice not in (1, 2, 3, 4, 5):
            print("Invalid choice.")
            continue
        else:
            break
    clear()

    return choice

def menu():
    choice = 0
    print("What would you like to do?")
    print("""(1) Create a new flashcard set
(2) Review a flashcard set
(3) Edit a flashcard set
(4) Delete a flashcard set
(5) Exit""")
    
    choice = getChoice()
    clear()
    if choice == 1:
        createSet()
    elif choice == 2:
        reviewSet()
    elif choice == 3:
        editSet()
    elif choice == 4:
        deleteSet()
    else:
        return 5
    clear()



print("Welcome to Flashcard Maker!")
flag = menu()
while flag != 5:
    flag = menu()