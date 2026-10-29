characters = {}

def create_character():
    while True:
        name = input("Enter new character name: ").strip()

        if name == "":
            print("Name cannot be empty")
        elif name in characters:
            print("Name already in use, try a different one")
        else:
            character = {
                "name": name,
                "attack": 20,
                "defense": 10,
                "hp": 100,
                "max_hp": 100,
                "rooms_explored": 0,
                "weapon": None,
                "shield": None
            }
            characters[name] = character
            return character


def load_character():
    if not characters:
        print("There are no saved characters yet.")
        return None

    names = list(characters)
    while True:
        print("\nSaved characters")
        print("-" * 45)
        for index, name in enumerate(names, start=1):
            character = characters[name]
            status = "Dead" if character["hp"] == 0 else "Alive"
            print(
                f'{index}) {name}'
                f' | HP: {character["hp"]}/{character["max_hp"]}'
                f' | Rooms Explored: {character["rooms_explored"]} | {status}'
            )
        print("0) Back")
        choice = input("Choose character: ").strip()
        if choice == "0":
            return None
        try:
            number = int(choice)
        except ValueError:
            print("Enter a number from the list.")
            continue
        if number < 1 or number > len(names):
            print("Enter a number from the list.")
            continue
        character = characters[names[number - 1]]
        if character["hp"] == 0:
            print("This character is dead and cannot continue.")
            continue
        print(f'Welcome back, {character["name"]}!')
        return character
