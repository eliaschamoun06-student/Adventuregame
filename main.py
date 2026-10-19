def splash():
    print()
    print("             Dungeon Quest")
    print()
    print("   1           2            3          4")
    print("New game - Load Game - Leaderboard - Quit")
    print()

def choose_option():

    x = input("Choose option: ")
    if(x == "1"):
        print("New Game") #koppla till Newgame function
    elif(x == "2"):
        print("Load Game") #koppla till Loadgame function
    elif(x == "3"):
            print("Leaderboard") #koppla till Leaderboard function
    elif(x == "4"):
            print("Quit") #koppla till Quit function
    else:
        print("Invalid input")
        print()
        choose_option()

    

def main():
    
    splash()
    choose_option()

    
    

main()
