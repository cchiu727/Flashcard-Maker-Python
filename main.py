# main.py
def getChoice():
    while True:
        try:
            choice = int(input("Enter a choice: "))
        except ValueError:
            print("Invalid choice.")
            continue
        if choice not in (1, 2, 3, 4):
            print("Invalid choice.")
            continue
        else:
            break
    return choice

def menu():
    choice = 0
    print("What would you like to do?")
    print("""   (1) Create a new flashcard set
        (2) Review a flashcard set
        (3) Edit a flashcard set
        (4) Delete a flashcard set""")
    
    choice = getChoice()


print("Welcome to Flashcard Maker!")
menu()
