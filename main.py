# main.py

def menu():
    choice = 0
    print("What would you like to do?")
    print("""   (1) Create a new flashcard set
        (2) Review a flashcard set
        (3) Edit a flashcard set
        (4) Delete a flashcard set""")
    choice = input("Enter a choice: ")
    print(choice)


print("Welcome to Flashcard Maker!")
menu()
