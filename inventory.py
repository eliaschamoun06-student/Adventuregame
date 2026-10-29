def offer_equipment(character, found_item):
    slot = found_item["type"]
    current_item = character[slot]

    print(f'\nYou found: {found_item["name"]}')
    print(f'Attack: +{found_item["attack"]}, Defense: +{found_item["defense"]} \n')

    if current_item is None:
        print("Currently equipped: nothing \n")
    else:
        print(f'Currently equipped: {current_item["name"]}')
        print(f'Attack: +{current_item["attack"]}, Defense: +{current_item["defense"]} \n')

    print("1) Equip found item")
    print("2) Keep current equipment")

    while True:
        choice = input("Choose: ").strip()
        if choice == "1":
            character[slot] = found_item.copy()
            print(f'You equipped {found_item["name"]}.')
            return
        elif choice == "2":
            print("You leave the found item behind.")
            return
        print("Invalid input")


def get_stat(character, stat):
    total = character[stat]
    for slot in ("weapon", "shield"):
        item = character[slot]
        if item is not None:
            total += item[stat]
    return total


def show_equipment(character):
    for slot in ("weapon", "shield"):
        item = character[slot]
        name = "Nothing" if item is None else item["name"]
        print(f"{slot.capitalize()}: {name}")

    print(f'Attack: {get_stat(character, "attack")}')
    print(f'Defense: {get_stat(character, "defense")}')
