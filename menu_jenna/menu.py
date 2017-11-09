WHO = 1
WHAT = 2
WHERE = 3
WHEN_LOVE = 4
WHY = 5
QUIT_CHOICE = 6

def main():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = input("Enter your decision: ")
        output = handle_choice(choice)
        print(output)

def display_menu():
    print("MENU")
    print("1)Who?")
    print("2)What?")
    print("3)Where?")
    print("4)When?")
    print("5)Why?")
    print("6)Quit")

def handle_choice(choice):
    if choice == WHO:
        queen = str(input("Would you like to be Beyonce? Answer Y for yes and N for no. "))
        if queen.upper() == 'Y':
            return "I am Beyonce. Always. "
        elif queen.upper() == 'N':
            return "Good. " + "I am Beyonce. Always. "
    elif choice == WHAT:
        life = int(input("Would you rather be a 10 or a 42?"))
        if life == 10:
            bears = str(input("Would you like to hear about bears? Answer Y for yes or  N for no. "))
            if bears.upper() == 'Y':
                return "Jim 'What bear is best?'" + " Dwight 'That’s a ridiculous question.' "+ " Jim 'False. Black Bear.' " + " Dwight 'That’s debatable. There are basically two schools of thought–' " + " Jim 'Fact. Bears eat beets. Bears. Beets. Battlestar Galactica.'"
            elif bears.upper() == 'N':
                return "That's no fun. I guess you don't like bears"
        elif life == 42:
            return "You are the answer to life, the universe, and everything"
    elif choice == WHERE:
        return "WHERE ARE THE TURTLES?!"
    elif choice == WHEN_LOVE:
        return "Do I want to be feared or loved? Um... easy, both. I want people to be afraid of how much they love me."
    elif choice == WHY:
        return "Well Happy Birthday, Jesus. Sorry your party's so lame."
    elif choice == QUIT_CHOICE:
        return "Exiting the Matrix..."
    elif choice != WHO or WHAT or WHERE  or WHEN_LOVE or WHY or QUIT_CHOICE:
        return "Error: Invalid entry. Get it together. "


main()