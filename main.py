import exploration
import inventory
import player


def splash_main_menu():

    print()
    print("             Dungeon Quest")
    print()
    print("   1           2            3          4")
    print("New game - Load Game - Leaderboard - Quit")
    print()

def splash_game_loop(character):
    print()
    print("R.E " + str(character["rooms_explored"]))
    print("             Dungeon Quest")
    print()
    print("       What are you going to do?")
    print()
    print("   1          2        3      4")
    print("Explore - Inventory - Shop - Quit")
    print()

def choose_option():
    while True:
        x = input("Choose option: ").strip()
        print()
        if x in ("1", "2", "3", "4"):
            return int(x)
        print("Invalid input")
        print()


def game_loop(character):
    loopedgame = True

    while loopedgame:
        splash_game_loop(character)

        choice = choose_option()

        if choice == 1:
            result = exploration.room_event(character)
            if result is False:
                print("Game Over")
                return
        elif choice == 2:
            inventory.show_equipment(character)
            print()
            input("Press `Enter` to continue!")
        elif choice == 3:
            print("shop")
        elif choice == 4:
            print("Game Quit")
            loopedgame = False


def main():
    while True:
        splash_main_menu()
        option = choose_option()

        if option == 1:  # New Game
            character = player.create_character()
            print("Your character name is " + character["name"])
            game_loop(character)
        elif option == 2:  # Load Game
            character = player.load_character()
            if character is not None:
                game_loop(character)
        elif option == 3:  # Leaderboard
            print("Leaderboard is not implemented yet")
        elif option == 4:  # Quit
            return


if __name__ == "__main__":
    main()
