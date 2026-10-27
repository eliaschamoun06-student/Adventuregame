import player  


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
        return 1
    elif(x == "2"):
        print("Load Game") #koppla till Loadgame function
        return 2
    elif(x == "3"):
        print("Leaderboard") #koppla till Leaderboard function
        return 3
    elif(x == "4"):
        print("Quit") #koppla till Quit function
        return 4
    else:
        print("Invalid input")
        print()
        choose_option()
    

def main():
    gametrue = True
    option = 0

    while(gametrue):
        splash()
        option = choose_option()

        if(option == 1): #New Game
            character = player.create_character()
            print(character)
            gametrue = False
        elif(option == 2): #Load Game
            gametrue = False
        elif(option == 3): #Leaderboard
            print("leaderboard")
            gametrue = False
        elif(option == 4): #Quit
            gametrue = False

    


    
main()
