WHO = 1
WHAT = 2
WHERE = 3
WHEN_LOVE = 4
WHY = 5
ADVICE= 6
QUIT_CHOICE = 7

def main():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = float(input("Enter your decision: "))
        output = handle_choice(choice)
        print(output)


def display_menu():
    print("MENU")
    print("Would you like to hear ...")
    print("1)Who?")
    print("2)What?")
    print("3)Where?")
    print("4)When?")
    print("5)Why?")
    print("6)Advice?")
    print("7)Quit")

def handle_choice(choice):
    if choice == WHO:
       queen = handle_who()
       print(queen)
    elif choice == WHAT:
        yeah= handle_what()
        print(yeah)
    elif choice == WHERE:
        donde = handle_where()
        print(donde)
    elif choice == WHEN_LOVE:
        fear = handle_when()
        print(fear)
    elif choice == WHY:
        lame = handle_why()
        print(lame)
    elif choice == ADVICE:
        advice_e = advice()
        print(advice_e)
    elif choice == QUIT_CHOICE:
        return "Exiting the Matrix..."
    else:
        return "Nope. That entry is invalid"

def handle_who():
    queen = str(input("Would you like to be Beyonce? "))
    if queen in ['y', 'yes', 'Y', 'Yes']:
        return "I am Beyonce. Always. "
    elif queen in ['n', 'N', 'No', 'no']:
        return "Good. " + "I am Beyonce. Always. "
    else:
        return "Error: Invalid Entry"

def handle_what():
    life = int(input("Would you rather be a 10 or a 42?"))
    if life == 10:
        bears = str(input("Would you like to hear about bears? "))
        if bears in ['y', 'yes', 'Y', 'Yes']:
            return "Jim 'What bear is best?'" + " Dwight 'That’s a ridiculous question.' "+ " Jim 'False. Black Bear.' " + \
            " Dwight 'That’s debatable. There are basically two schools of thought–' " + " Jim 'Fact. Bears eat beets. Bears. Beets. Battlestar Galactica.'"
        elif bears in ['n', 'N', 'No', 'no']:
            return "That's no fun. I guess you don't like bears"
        else:
            return "That entry isn't valid you litle plop. "
    elif life == 42:
        return "You are the answer to life, the universe, and everything"
    else:
        return "You need to get it together, you little Flapjack Palmdale. That entry isn't valid. "

def handle_where():
    turtles= input("Do you like turtles? ")
    if turtles in ['y', 'yes', 'Y', 'Yes']:
        return "WHERE ARE THE TURTLES?!"
    elif turtles in ['n', 'N', 'No', 'no']:
        return "You are wrong. Turtles are great and need more love and attention. "
    else:
        return "That isn't valid you oatmeal raisin cookie. "
        
def handle_when():
    cookies = input("Do you like oatmeal raisin cookies?")
    if cookies in ['y', 'yes', 'Y', 'Yes']:
        return "What is wrong with you? "
    elif cookies in ['n', 'N', 'No', 'no']: 
        return " Good. You are a person. Here's an Office quote." + "Do I want to be feared or loved? Um... easy, both. I want people to be afraid of how much they love me."
    else:
        return " That entry isn't valid famss"

def handle_why():
    birthday = input("Is it your birthday today?")
    if birthday in ['y', 'yes', 'Y', 'Yes']:
       jesus_you = jesus()
       print(jesus_you)
    elif birthday in ['n', 'N', 'No', 'no']:
        liar = input("Are you lying?")
        if liar in  ['y', 'yes', 'Y', 'Yes']:
            lying_liar_who_lies = jesus()
            print(lying_liar_who_lies)
        elif liar in ['n', 'N', 'No', 'no']:
            return "Well thats no fun. You don't get birthday cake, but you go live your life like it's your birthday. "
        else:
            return "That isn't a valid entry. Please try again."
    else:
        return "That entry isn't valid, try again. "


def jesus():
    jesus = input("Are you Jesus?")
    if jesus in ['y', 'yes', 'Y', 'Yes']:
        return "Well Happy Birthday, Jesus. Sorry your party's so lame."
    elif jesus in ['n', 'N', 'No', 'no']:
        return " Okay. Happy Birthday and you do you BooBoo"
    else:
        return "Nah man. That input isn't valid. "

def advice():
    advice_please = input("Would you like to hear some advice? ")
    if advice_please in ['y', 'yes', 'Y', 'Yes']:
        select_person = input("Would you like to hear advice from Bill Nye or Michael Scott? ")
        if select_person in ['nye', 'bill', 'Bill', 'Nye', 'Bill Nye', 'Bill nye', 'bill Nye', 'The Science Guy', 'Bill Nye the Science Guy']:
            return "My father and mother emphasized two things: Every person is responsible for his or her own actions, and, to the best of your ability, leave the world better than you found it." + \
            "That's why I say that sometimes you've got to pick up other people's trash. Just because somebody else filled the atmosphere with carbon dioxide is no reason not to address the problem." + \
            "We're all in this together. After you use the paper towel, put it in the trash can. OK, can we all do that?" + "-Bill Nye"
        elif select_person in ['Michael', 'Scott', 'Michael Scott', 'michael scott', 'the guy from the Office', 'that guy from the office']:
            return "It's never to early for ice cream" + "-Michael Scott"
        else:
            return "That is not a person you can chose. Try again."
    elif advice_please in ['n', 'N', 'No', 'no']:
        return 'Well, why did you pick this one then?'
    else:
        return "That wasn't a valid option. Try again. "

main()