characters = {}

character_types = {
    "1": {
        "type": "Elf",
        "attack": 27,
        "defense": 8,
        "hp": 110
    },
    "2": {
        "type": "Human",
        "attack": 25,
        "defense": 9,
        "hp": 115
    },
    "3": {
        "type": "Dwarf",
        "attack": 23,
        "defense": 10,
        "hp": 120
    },
    "4": {
        "type": "Orc",
        "attack": 28,
        "defense": 7,
        "hp": 115
    },
    "5": {
        "type": "Halfling",
        "attack": 24,
        "defense": 10,
        "hp": 105
    },
    "6": {
        "type": "Goblin",
        "attack": 28,
        "defense": 8,
        "hp": 100
    }
}


def choose_character_type():
    print("\nChoose character type:")

    for number, character_type in character_types.items():
        print(
            f'{number}) {character_type["type"]}'
            f' | Attack: {character_type["attack"]}'
            f' | Defense: {character_type["defense"]}'
            f' | HP: {character_type["hp"]}'
        )

    while True:
        choice = input("Choose: ").strip()

        if choice in character_types:
            return character_types[choice]

        print("Invalid choice, try again.")


def create_character():
    while True:
        name = input("Enter new character name: ").strip()

        if name == "":
            print("Name cannot be empty")
        elif name in characters:
            print("Name already in use, try a different one")
        else:
            character_type = choose_character_type()

            character = {
                "name": name,
                "type": character_type["type"],
                "attack": character_type["attack"],
                "defense": character_type["defense"],
                "hp": character_type["hp"],
                "max_hp": character_type["hp"],
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
                f' | Type: {character["type"]}'
                f' | HP: {character["hp"]}/{character["max_hp"]}'
                f' | Rooms Explored: {character["rooms_explored"]}'
                f' | {status}'
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