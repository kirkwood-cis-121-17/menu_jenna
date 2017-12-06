QUIT_CHOICE = 6
def main():
    choice = 0
    while choice != QUIT_CHOICE:
        DUMP_TRUCKS = 1
        BLENDERS= 2
        TOILETS = 3
        NORTH_POLE = 4
        BIRTHDAYS= 5
        display_menu()
        choice = float(input("Enter your decision: "))
        output = handle_choice(choice)
        print(output)
        print("All information comes from Wikipedia. You're welcome. ")


def display_menu():
    print("MENU")
    print("What would you like to learn about?")
    print("1)Dump Trucks")
    print("2)Blenders")
    print("3)Toilets")
    print("4)North Pole")
    print("5)Birthdays")
    print("6)Quit")

def handle_choice(choice):
    DUMP_TRUCKS = 1
    BLENDERS= 2
    TOILETS = 3
    NORTH_POLE = 4
    BIRTHDAYS= 5
    QUIT_CHOICE = 6
    if choice == DUMP_TRUCKS:
       dump_trucks_menu()
    elif choice == BLENDERS:
        blenders_menu()
    elif choice == TOILETS:
        toilets_menu()
    elif choice == NORTH_POLE:
        north_pole_menu()
    elif choice == BIRTHDAYS:
        birthdays_menu()
    elif choice == QUIT_CHOICE:
        return "Exiting the Matrix..."
    else:
        return "Nope. That entry is invalid"
        
def dump_trucks_menu():
    HISTORY = 1
    DANGERS = 2
    TYPES = 3
    MOVIES = 4
    
    def dump_trucks_display():
        print("MENU")
        print("What would you like to learn about dump trucks?")
        print("1)History")
        print("2)Dangers")
        print("3)Types")
        print("4)In Movies")
        print("6)Quit")
    
    def main_dump_trucks():
        choice = 0
        while choice != QUIT_CHOICE:
            dump_trucks_display()
            choice = float(input("Enter your decision: "))
            output = handle_dump_trucks(choice)
            print(output)
            

    def handle_dump_trucks(choice):
        HISTORY = 1
        DANGERS = 2
        TYPES = 3
        MOVIES = 4
        if choice == HISTORY:
            sass = dump_trucks_history()
            print(sass)
        elif choice == DANGERS:
            z = dump_trucks_dangers()
            print(z)
        elif choice == TYPES:
            x = dump_trucks_types()
            print(x)
        elif choice == MOVIES:
            c = dump_trucks_movies()
            print(c)
        elif choice == QUIT_CHOICE:
            return " Exiting the program"
        else:
            return "What was that? That wasn't an option."

    main_dump_trucks()

def dump_trucks_history():
    return "AAAAA DUMP TRUCKS"
def dump_trucks_dangers():
    return " Scare Scare"
def dump_trucks_types():
    return "brand brand"
def dump_trucks_movies():
    return "film film"


def blenders_menu():
    HISTORY = 89
    DANGERS = 33
    TYPES = 42
    MOVIES = 204
    
    def blenders_display():
        print("MENU")
        print("What would you like to learn about dump trucks?")
        print("89)History")
        print("33)Dangers and Accidents")
        print("42)Types")
        print("204)In Movies")
        print("6)Quit")
    
    def main_blenders():
        choice = 0
        while choice != QUIT_CHOICE:
            blenders_display()
            choice = float(input("Enter your decision: "))
            output = handle_blenders(choice)
            print(output)
            

    def handle_blenders(choice):
        if choice == HISTORY:
            x=blenders_history()
            print(x)
        elif choice == DANGERS:
            q = blenders_dangers()
            print(q)
        elif choice == TYPES:
            a = blenders_types()
            print(a)
        elif choice == MOVIES:
            s = blenders_movies()
            print(s)
        elif choice == QUIT_CHOICE:
            return " Exiting the program"
        else:
            return "What was that? That wasn't an option."
    main_blenders()

def blenders_history():
    return "They came into being"
def blenders_dangers():
    return "They can break down your food and your hand"
def blenders_types():
    return "Regular or small"
def blenders_movies():
    return "In movies people keep sticking their hands in blenders"

def toilets_menu():
    HISTORY = 1
    DANGERS = 2
    TYPES = 3
    MOVIES = 4
    
    def toilets_display():
        print("MENU")
        print("What would you like to learn about toilets?")
        print("1)History")
        print("2)Dangers and Accidents")
        print("3)Types")
        print("4)In Movies")
        print("6)Quit")
    
    def main_toilets():
        choice = 0
        while choice != QUIT_CHOICE:
            toilets_display()
            choice = float(input("Enter your decision: "))
            output = handle_toilets(choice)
            print(output)
            

    def handle_toilets(choice):
        if choice == HISTORY:
            a = toilets_history()
            print(a)
        elif choice == DANGERS:
            b = toilets_dangers()
            print(b)
        elif choice == TYPES:
            c = toilets_types()
            print(c)
        elif choice == MOVIES:
            d = toilets_movies()
            print(d)
        elif choice == QUIT_CHOICE:
            return " Exiting the program"
        else:
            return "What was that? That wasn't an option."
    main_toilets()

def toilets_history():
    return "OUthouse to turlet"
def toilets_dangers():
    return "You can get stuck"
def toilets_types():
    return "Toilets"
def toilets_movies():
    return " Poeple go potty"
    

def north_pole_menu():
    HISTORY = 1
    DANGERS = 2
    CREATURES = 3
    MOVIES = 4
    
    def north_pole_display():
        print("MENU")
        print("What would you like to learn about the North Pole?")
        print("1)History")
        print("2)Dangers")
        print("3)Creatures")
        print("4)In Movies")
        print("6)Quit")
    
    def main_north_pole():
        choice = 0
        while choice != QUIT_CHOICE:
            north_pole_display()
            choice = float(input("Enter your decision: "))
            output = handle_north_pole(choice)
            print(output)
            

    def handle_north_pole(choice):
        if choice == HISTORY:
            q = north_pole_history()
            print(q)
        elif choice == DANGERS:
            w = north_pole_dangers()
            print(w)
        elif choice == CREATURES:
            e = north_pole_creatures()
            print(e)
        elif choice == MOVIES:
            r = north_pole_movies()
            print(r)
        elif choice == QUIT_CHOICE:
            return " Exiting the program"
        else:
            return "What was that? That wasn't an option."
    main_north_pole()

def north_pole_history():
    return "Santa moved there and explorers die"
def north_pole_dangers():
    return "Reindeer????"
def north_pole_creatures():
    return "Bears"
def north_pole_movies():
    return "Every Christmas Movie Ever"
    
def birthdays_menu():
    HISTORY = 1
    DANGERS = 2
    TYPES = 3
    MOVIES = 4
    
    def birthdays_display():
        print("MENU")
        print("What would you like to learn about Birthdays?")
        print("1)History")
        print("2)Dangers")
        print("3)Types")
        print("4)In Movies")
        print("6)Quit")
    
    def main_birthdays():
        choice = 0
        while choice != QUIT_CHOICE:
            birthdays_display()
            choice = float(input("Enter your decision: "))
            output = handle_birthdays(choice)
            print(output)
            

    def handle_birthdays(choice):
        if choice == HISTORY:
            a = birthdays_history()
            print(a)
        elif choice == DANGERS:
            s = birthdays_dangers()
            print(s)
        elif choice == TYPES:
            d = birthdays_types()
            print(d)
        elif choice == MOVIES:
            f = birthdays_movies()
            print(f)
        elif choice == QUIT_CHOICE:
            return " Exiting the program"
        else:
            return "What was that? That wasn't an option."
            
    main_birthdays()

def birthdays_history():
    return "They happen once a year for everybody"
def birthdays_dangers():
    return "You are aging. Therefore you are dying."
def birthdays_types():
    return " Feliz Cumpleaños"
def birthdays_movies():
    return "Sixteen Candles, Happy Death Day"



main()