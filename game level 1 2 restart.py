def playagain():
    restart = input("Would you like to play again?")
    if restart == "y":
        startgame()
    else:
        print("goodbye")
    
def startgame():
    choice = input("Which do you choose?")
    if choice == "a":
        print("Good!")
        leveltwo()
    elif choice == "b":
        print("Bad!")
        playagain()

def leveltwo():
    print("This is level two.")
    choice = input("Do you want to go back to level one?")
    if choice == "y":
        print("OK, back to level one we go.")
        startgame()
    else:
        print("Nevermind then.")

        
startgame()
    
