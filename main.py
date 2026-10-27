import player  
import exploration
import inventory
import shop
import combat

def splash_main_menu():

    print()
    print("             Dungeon Quest")
    print()
    print("   1           2            3          4")
    print("New game - Load Game - Leaderboard - Quit")
    print()

def splash_game_loop():
    print("             Dungeon Quest")
    print()
    print("       What are you going to do?")
    print()
    print("   1          2        3      4")
    print("Explore - Inventory - Shop - Quit")
    print()

def choose_option():

    x = input("Choose option: ")
    if(x == "1"):
        return 1
    elif(x == "2"):
        return 2
    elif(x == "3"):
        return 3
    elif(x == "4"):
        return 4
    else:
        print("Invalid input")
        print()
        choose_option()

def game_loop():
    loopedgame = True

    while loopedgame:
        splash_game_loop()

        choice = choose_option()

        if choice == 1:
            print("explore")
        elif choice == 2:
            print("inventory")
        elif choice == 3:
            print("shop")
        elif choice == 4:
            print("Game Quit")
            loopedgame = False


def main():

    gametrue = True

    while(gametrue):
        splash_main_menu()
        option = choose_option()

        if(option == 1): #New Game
            character = player.create_character()
            print("Your character name is " + character["name"])
            combat.combat(character)
            gametrue = False
        elif(option == 2): #Load Game
            gametrue = False
        elif(option == 3): #Leaderboard
            print("leaderboard")
            gametrue = False
        elif(option == 4): #Quit
            gametrue = False

    
    game_loop()

    
main()
