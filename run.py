# Import the module
import random


#Welcome message, game rules and player name
print("Welcome to game world")

player = input("Do you want to play Rock, Paper, Scissors game? yes/no ")

if player.lower() != "yes":
    quit("Thanks for stoping by")
else:
    print("Here is the rules for the game ")  
    print(" . The game is between you and the computer")
    print()
    print(" . There are 5 options to chose from (Fire, Wave, Fish, Boat, Grass)")
    print()
    print(" . You chose one and computer choses randomly")
    print()
    print(" . If your choice is same as the computer, you lose.")
    print()
    print(" . If your choice beats computer chose, you wine if not you lose")
    print()

player = input(" . If you are ready, type 'ok' ")

if player.lower() != "ok":
    quit("Okay, thanks for stopping by")
else:
    print("Game starts :)")
print()   
# Let player enter name
name = input("Enter your name ").capitalize()
# The strip() method ensures that something has to be entered and
# the isalpha() method ensures that only letters can be entered
while not name.strip() or not name.isalpha():
    name = input("The input field must not be left blank.\n"
                      "The user name must not contain any spaces, "
                      "only letters are permitted!\n"
                      "Please enter your Name:\n")
print()
"Name: "
print("Hi,", str(name) + "!")
#End player name

# Player score
played = 0
won = 0
lost = 0
tie = 0

# Add player and computer choice
options = ("fire", "wave", "fish", "boat", "grass")

# Let user play again
running = True

while running:
    playerchoice = None
    computerchoice = random.choice(options) #Computer choses randomly

    while playerchoice not in options: # Keep runing until player chose from optionlist
        playerchoice = input("Make a choice (Fire, Wave, Fish, Boat, Grass) ").lower()

    if playerchoice == "fire":
        print('''You chose '''+playerchoice+'''!''') #Print player choice
        print('''
    ⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀
    ⠀⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀
    ⠀⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀
    ⠀⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆
    ⢰⢀⣾⣿⣿⠟⠀⠀⣾⢿⣿⣿⣿⣿
    ⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿⡿
    ⢳⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⡿⡁
    ⠀⠹⣿⣿⡄⠀⠀⠀⠀⠀⢠⣿⡞⠁
    ⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠞⠋⠀⠀
    ⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀
        ''')

    elif playerchoice == "wave":
        print('''You chose '''+playerchoice+'''!''') #Print player choice
        print('''⢠⠦⠴⠂⠒⠲⠙⠒⠶⠤⢄⡀⢀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢤⣀⠀⠀⠀
    ⠀⠀⠈⣧⠀⠀⠀⠀⣀⢄⣶⣿⣿⣷⣦⡄⠀⠀⠀⠈⡄⠀⠀
    ⠀⠀⠀⠑⠒⠓⠒⠋⠁⠀⠀⠘⣿⠙⢹⣷⣦⣀⠀⠀⠙⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⠸⣿⣿⣿⣾⣇⠀⢄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣇⠸⣿⣿⢻⣿⡄⠸⡀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠟⠙⡀⣿⠛⢰⢻⡇⠐⡅
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⡞⠀⢰⣿⣿⡃⣼⣿⣿⢧⠁
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⢀⢠⣿⡾⣹⣽⠉⣧⣿⡎⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣮⢂⣾⡿⣃⠃⠃⣸⣿⡾⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⡾⡡⣱⣿⢯⣾⣿⢯⢏⣾⣷⢯⡿⠁⠀⠀
    ⠀⢀⣀⣤⠶⠟⡩⣾⣴⡿⢗⣽⢟⠏⣼⣽⣿⣷⠟⠀⠀⠀⠀
    ⠉⠙⠫⠠⠔⠮⠬⠽⠿⠴⣟⠅⠡⠾⠧⠿⠟⠁⠀⠀⠀⠀⠀⠀
        ''')

    elif playerchoice == "fish":
        print('''You chose '''+playerchoice+'''!''') #Print player choice
        print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡀⠀⠀⠀⠀
    ⠈⣿⣶⣤⡀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀
    ⠀⢹⣿⣿⣿⣷⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
    ⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀
    ⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
    ⠀⢸⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀
    ⠀⣿⣿⠿⠋⠁⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀
    ⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡿⠿⠟⠋⠉⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')

    elif playerchoice == "boat":
        print('''You chose '''+playerchoice+'''!''') #Print player choice
        print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡧⣬⢿⡇⠀⣿⠬⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢡⠃⠀⢇⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⣌⡎⣩⡉⡉⡉⢉⢉⠉⢣⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⠤⠼⠼⠝⡸⠹⠿⠇⠇⠿⠸⠀⠘⠦⡀⠀⠀⠀⠀⠀
    ⢀⣠⣤⣤⣤⣤⣤⣎⣜⣁⣀⣀⣁⣀⣀⣀⣀⣀⣀⣀⣀⣀⣙⣦⣤⣤⣀⡀
    ⢸⡁⢹⣼⣯⡀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣿⡇
    ⠘⢦⣈⣶⡷⢂⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣜⡾⠁
    ⠀⠘⢏⠉⠫⡉⠉⠁⠀⠐⠛⠛⠛⠛⠛⠛⠛⠛⠃⠈⠽⠯⠭⢭⣯⡟⠁⠀
    ⠀⠀⠈⠳⣄⡈⠒⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠋⠀⠀⠀
    ⠀⠀⠀⠀⠀⠉⠉⠀⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠂⠉⠉⠁⠀⠀⠀⠀⠀⠀
        ''')

    if playerchoice == "grass":
        print('''You chose '''+playerchoice+'''!''') #Print player choice
        print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢠⡇⠀⠀⡆⠀⠀⠀⠀⠀⢀⠀⠀⣼⣿⠀⠀⠀⢰⠀⠀⠀⢀⡇⠀⠀⠀⠀
    ⠀⠀⢸⡇⠀⠀⣷⠀⠀⢠⠀⠀⣸⡀⠀⣿⣿⠀⠀⠀⣼⡇⠀⠀⣼⠀⠀⢠⡆⠀
    ⠀⠀⣼⡇⠀⠀⣿⡆⠀⣾⠀⠀⣿⡇⢀⣿⣿⠀⠀⠀⣿⣿⠀⢀⣿⡇⠀⢸⡇⠀
    ⠀⠀⣿⣇⠀⢠⣿⣧⢀⣿⠀⢰⣿⡇⢸⣿⣿⡇⠀⢠⣿⣿⡆⢸⣿⡇⠀⣿⣷⠀
    ⠀⢀⣿⣿⠀⢸⣿⣿⢸⣿⡄⣼⣿⣷⢸⣿⣿⣿⣀⣾⣿⣿⡇⣿⣿⣷⢰⣿⣿⠀
    ⠀⢸⣿⣿⡇⢸⣿⣿⣾⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⠀
    ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
    ⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀
        ''')


    computerchoice = random.randint(1,5) # List computer choice in number 1-5
    if computerchoice == 1:
        print('''The computer chose fire!''') #print computer choice
        print('''
    ⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀
    ⠀⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀
    ⠀⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀
    ⠀⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆
    ⢰⢀⣾⣿⣿⠟⠀⠀⣾⢿⣿⣿⣿⣿
    ⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿⡿
    ⢳⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⡿⡁
    ⠀⠹⣿⣿⡄⠀⠀⠀⠀⠀⢠⣿⡞⠁
    ⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠞⠋⠀⠀
    ⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀
        ''')

    elif computerchoice == 2:
        print('''The computer chose wave!''')
        print('''⢠⠦⠴⠂⠒⠲⠙⠒⠶⠤⢄⡀⢀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢤⣀⠀⠀⠀
    ⠀⠀⠈⣧⠀⠀⠀⠀⣀⢄⣶⣿⣿⣷⣦⡄⠀⠀⠀⠈⡄⠀⠀
    ⠀⠀⠀⠑⠒⠓⠒⠋⠁⠀⠀⠘⣿⠙⢹⣷⣦⣀⠀⠀⠙⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⠸⣿⣿⣿⣾⣇⠀⢄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣇⠸⣿⣿⢻⣿⡄⠸⡀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠟⠙⡀⣿⠛⢰⢻⡇⠐⡅
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⡞⠀⢰⣿⣿⡃⣼⣿⣿⢧⠁
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⢀⢠⣿⡾⣹⣽⠉⣧⣿⡎⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣮⢂⣾⡿⣃⠃⠃⣸⣿⡾⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⡾⡡⣱⣿⢯⣾⣿⢯⢏⣾⣷⢯⡿⠁⠀⠀
    ⠀⢀⣀⣤⠶⠟⡩⣾⣴⡿⢗⣽⢟⠏⣼⣽⣿⣷⠟⠀⠀⠀⠀
    ⠉⠙⠫⠠⠔⠮⠬⠽⠿⠴⣟⠅⠡⠾⠧⠿⠟⠁⠀⠀⠀⠀⠀
        ''')

    elif computerchoice == 3:
        print('''The computer chose fish!''')
        print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡀⠀⠀⠀⠀
    ⠈⣿⣶⣤⡀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀
    ⠀⢹⣿⣿⣿⣷⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
    ⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀
    ⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
    ⠀⢸⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀
    ⠀⣿⣿⠿⠋⠁⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀
    ⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡿⠿⠟⠋⠉⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')

    elif computerchoice == 4:
        print('''The computer chose boat!''')
        print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡧⣬⢿⡇⠀⣿⠬⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢡⠃⠀⢇⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⣌⡎⣩⡉⡉⡉⢉⢉⠉⢣⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⠤⠼⠼⠝⡸⠹⠿⠇⠇⠿⠸⠀⠘⠦⡀⠀⠀⠀⠀⠀
    ⢀⣠⣤⣤⣤⣤⣤⣎⣜⣁⣀⣀⣁⣀⣀⣀⣀⣀⣀⣀⣀⣀⣙⣦⣤⣤⣀⡀
    ⢸⡁⢹⣼⣯⡀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣿⡇
    ⠘⢦⣈⣶⡷⢂⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣜⡾⠁
    ⠀⠘⢏⠉⠫⡉⠉⠁⠀⠐⠛⠛⠛⠛⠛⠛⠛⠛⠃⠈⠽⠯⠭⢭⣯⡟⠁⠀
    ⠀⠀⠈⠳⣄⡈⠒⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠋⠀⠀⠀
    ⠀⠀⠀⠀⠀⠉⠉⠀⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠂⠉⠉⠁⠀⠀⠀⠀⠀⠀
        ''')

    elif computerchoice == 5:
        print('''The computer chose grass!''')
        print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢠⡇⠀⠀⡆⠀⠀⠀⠀⠀⢀⠀⠀⣼⣿⠀⠀⠀⢰⠀⠀⠀⢀⡇⠀⠀⠀⠀
    ⠀⠀⢸⡇⠀⠀⣷⠀⠀⢠⠀⠀⣸⡀⠀⣿⣿⠀⠀⠀⣼⡇⠀⠀⣼⠀⠀⢠⡆⠀
    ⠀⠀⣼⡇⠀⠀⣿⡆⠀⣾⠀⠀⣿⡇⢀⣿⣿⠀⠀⠀⣿⣿⠀⢀⣿⡇⠀⢸⡇⠀
    ⠀⠀⣿⣇⠀⢠⣿⣧⢀⣿⠀⢰⣿⡇⢸⣿⣿⡇⠀⢠⣿⣿⡆⢸⣿⡇⠀⣿⣷⠀
    ⠀⢀⣿⣿⠀⢸⣿⣿⢸⣿⡄⣼⣿⣷⢸⣿⣿⣿⣀⣾⣿⣿⡇⣿⣿⣷⢰⣿⣿⠀
    ⠀⢸⣿⣿⡇⢸⣿⣿⣾⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⠀
    ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
    ⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀
        ''')

    # Add Winner condition
    if playerchoice == "fire" and computerchoice == 1:
        print("It's a tie!")
        tie = 0
        played += 1

    elif playerchoice == "fire" and computerchoice == 2:
        print("You lose!")
        lost += 1
        played += 1

    elif playerchoice == "fire" and computerchoice == 3:
        print("Yeah! you win")
        print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
    ⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
    ⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
    ⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
    ⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
    ⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
    ⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
    ⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        won += 1
        played += 1

    elif playerchoice == "fire" and computerchoice == 4:
        print("You lose!")
        lost += 1
        played += 1

    elif playerchoice == "fire" and computerchoice == 5:
        print("Yeah! you win")
        print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
    ⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
    ⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
    ⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
    ⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
    ⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
    ⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
    ⠀⠀⠈⣚⡻⠇
    ''')
        won += 1
        played += 1

    #Wave
    elif playerchoice == "wave" and computerchoice == 1:
        print("You lose!")
        lost += 1
        played += 1

    elif playerchoice == "wave" and computerchoice == 2:
        print("It's a tie!")
        tie = 0
        played += 1

    elif playerchoice == "wave" and computerchoice == 3:
        print("Yeah! you win")
        print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
    ⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
    ⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
    ⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
    ⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
    ⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
    ⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
    ⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        won += 1
        played += 1

    elif playerchoice == "wave" and computerchoice == 4:
        print("Yeah! you win")
        print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
    ⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
    ⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
    ⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
    ⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
    ⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
    ⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
    ⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        won += 1
        played += 1

    elif playerchoice == "wave" and computerchoice == 5:
        print("You lose!")
        lost += 1
        played += 1

    #Fish
    elif playerchoice == "fish" and computerchoice == 1:
        print("You lose!!")
        lost += 1
        played += 1

    elif playerchoice == "fish" and computerchoice == 2:
        print("Yeah! you win")
        print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
    ⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
    ⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
    ⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
    ⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
    ⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
    ⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
    ⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        won += 1
        played += 1
        

    elif playerchoice == "fish" and computerchoice == 3:
        print("Its a tie!")
        tie = 0
        played += 1

    elif playerchoice == "fish" and computerchoice == 4:
        print("Yeah! you win")
        print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
    ⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
    ⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
    ⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
    ⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
    ⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
    ⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
    ⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        won += 1
        played += 1

    elif playerchoice == "fish" and computerchoice == 5:
        print("You lose")
        lost += 1
        played += 1

    #Boat
    elif playerchoice == "boat" and computerchoice == 1:
        print("You lose!")
        lost += 1
        played += 1

    elif playerchoice == "boat" and computerchoice == 2:
        print("Yeah! you win")
        print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
    ⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
    ⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
    ⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
    ⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
    ⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
    ⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
    ⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        won += 1
        played += 1

    elif playerchoice == "boat" and computerchoice == 3:
        print("Yeah! you win")
        print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
    ⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
    ⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
    ⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
    ⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
    ⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
    ⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
    ⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        won += 1
        played += 1

    elif playerchoice == "boat" and computerchoice == 4:
        print("It's a tie!")
        tie += 1
        played += 1

    elif playerchoice == "boat" and computerchoice == 5:
        print("You lose!")
        lost += 1
        played += 1

    #Grass
    elif playerchoice == "grass" and computerchoice == 1:
        print("Yeah! you win")
        print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
    ⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
    ⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
    ⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
    ⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
    ⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
    ⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
    ⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        won += 1
        played += 1

    elif playerchoice == "grass" and computerchoice == 2:
        print("You lose!")
        lost += 1
        played += 1

    elif playerchoice == "grass" and computerchoice == 3:
        print("You lose!")
        lost += 1
        played += 1

    elif playerchoice == "grass" and computerchoice == 4:
        print("Yeah! you win")
        print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
    ⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
    ⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
    ⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
    ⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
    ⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
    ⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
    ⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        won += 1
        played += 1

    elif playerchoice == "grass" and computerchoice == 5:
        print("It's a tie!")
        tie += 1
        played += 1

    if not input("play again? (y/n): ").lower()== "y":
        running = False

    player_choice_result = playerchoice(name)
    computer_choice_result = computerchoice()
    find_winner(computer_choice_result, player_choice_result)
    game_end(won_games, lost_games, played_games, drawn_games)
