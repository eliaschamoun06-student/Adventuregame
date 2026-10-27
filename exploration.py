import random
import combat

events = ("spawn_monster", "spawn_chest")

chest_items = {
    "diamond_sword": {
        "damage": 25,
        "defense": 10
    },
    "iron_shield": {
        "defense": 35
    }
}


def choose_action():
    while True:
        choice = input("Choose: ").strip()
        if choice in ("1", "2"):
            return choice
        print("Invalid input")


def open_chest(character):
    item_name = random.choice(list(chest_items))
    item = chest_items[item_name]

    print(f"You have found {item_name}!")
    print("1) Equip")
    print("2) Leave")
    choice = choose_action()

    if choice == "1":
        character["attack"] += item.get("damage", 0)
        character["defense"] += item.get("defense", 0)


def room_event(character):
    event = random.choice(events)
    if event == "spawn_monster":
        print("A monster has appeared")
        print("1) Attack")
        print("2) Escape")
        choice = choose_action()
        if choice == "1":
            return combat.combat(character)
        else:
            print("You have escaped")
    elif event == "spawn_chest":
        print("You have found a chest!")
        print("1) Open")
        print("2) Leave")
        choice = choose_action()
        if choice == "1":
            open_chest(character)
