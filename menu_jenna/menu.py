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
        choice = float(input("Enter your decision: "))
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
        queen = str(input("Would you like to be Beyonce? "))
        if queen in ['y', 'yes', 'Y', 'Yes']:
            return "I am Beyonce. Always. "
        elif queen in ['n', 'N', 'No', 'no']:
            return "Good. " + "I am Beyonce. Always. "
        else:
            return "Error: Invalid Entry"
    elif choice == WHAT:
        life = int(input("Would you rather be a 10 or a 42?"))
        if life == 10:
            bears = str(input("Would you like to hear about bears? Answer Y for yes or  N for no. "))
            if bears.upper() == 'Y':
                return "Jim 'What bear is best?'" + " Dwight 'That’s a ridiculous question.' "+ " Jim 'False. Black Bear.' " + " Dwight 'That’s debatable. There are basically two schools of thought–' " + " Jim 'Fact. Bears eat beets. Bears. Beets. Battlestar Galactica.'"
            elif bears.upper() == 'N':
                return "That's no fun. I guess you don't like bears"
            else:
                return "That entry isn't valid you litle plop. "
        elif life == 42:
            return "You are the answer to life, the universe, and everything"
        else:
            return "You need to get it together, you little Flapjack Palmdale. That entry isn't valid. "
    elif choice == WHERE:
        turtles= input("Do you like turtles? ")
        if turtles in ['y', 'yes', 'Y', 'Yes']:
            return "WHERE ARE THE TURTLES?!"
        elif turtles in ['n', 'N', 'No', 'no']:
            return "You are wrong. Turtles are great and need more love and attention. "
        else:
            return "That isn't valid you oatmeal raisin cookie. "
    elif choice == WHEN_LOVE:
        return "Do I want to be feared or loved? Um... easy, both. I want people to be afraid of how much they love me."
    elif choice == WHY:
        return "Well Happy Birthday, Jesus. Sorry your party's so lame."
    elif choice == QUIT_CHOICE:
        return "Exiting the Matrix..."
    else:
        return "Nope. That entry is invalid"



main()