import enemies
import inventory


def calculate_damage(attack, defense):
    return max(1, attack - defense)


def combat(character):
    monster = enemies.random_monster(character["rooms_explored"])

    print(f'\nA {monster["name"]} appears!')

    while character["hp"] > 0 and monster["hp"] > 0:
        print(f'\n{character["name"]}: {character["hp"]} HP')
        print(f'{monster["name"]}: {monster["hp"]} HP')
        print("1) Attack")

        choice = input("Choose: ").strip()

        if choice != "1":
            print("Invalid input")
            continue

        # Player's turn
        damage = calculate_damage(
            inventory.get_stat(character, "attack"), monster["defense"]
        )
        monster["hp"] = max(0, monster["hp"] - damage)
        print(f'You deal {damage} damage!')

        # A defeated monster does not get a turn.
        if monster["hp"] == 0:
            character["rooms_explored"] += 1
            print(f'You defeated the {monster["name"]}!')
            return True

        # Monster's turn
        damage = calculate_damage(
            monster["attack"], inventory.get_stat(character, "defense")
        )
        character["hp"] = max(0, character["hp"] - damage)
        print(f'The {monster["name"]} deals {damage} damage!')

    print("Your character has died.")
    return False
