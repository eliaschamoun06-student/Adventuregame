import random

import combat
import inventory

events = ("spawn_monster", "spawn_chest")

chest_items = {
    "rusty_sword": {
        "name": "Rusty Sword",
        "type": "weapon",
        "attack": 2,
        "defense": 0
    },
    "wooden_sword": {
        "name": "Wooden Sword",
        "type": "weapon",
        "attack": 4,
        "defense": 0
    },
    "iron_sword": {
        "name": "Iron Sword",
        "type": "weapon",
        "attack": 6,
        "defense": 0
    },
    "steel_sword": {
        "name": "Steel Sword",
        "type": "weapon",
        "attack": 8,
        "defense": 0
    },
    "knights_sword": {
        "name": "Knight's Sword",
        "type": "weapon",
        "attack": 11,
        "defense": 0
    },
    "diamond_sword": {
        "name": "Diamond Sword",
        "type": "weapon",
        "attack": 14,
        "defense": 0
    },
    "flame_sword": {
        "name": "Flame Sword",
        "type": "weapon",
        "attack": 17,
        "defense": 0
    },
    "kings_sword": {
        "name": "King's Sword",
        "type": "weapon",
        "attack": 20,
        "defense": 0
    },
    "broken_shield": {
        "name": "Broken Shield",
        "type": "shield",
        "attack": 0,
        "defense": 1
    },
    "wooden_shield": {
        "name": "Wooden Shield",
        "type": "shield",
        "attack": 0,
        "defense": 2
    },
    "iron_shield": {
        "name": "Iron Shield",
        "type": "shield",
        "attack": 0,
        "defense": 4
    },
    "steel_shield": {
        "name": "Steel Shield",
        "type": "shield",
        "attack": 0,
        "defense": 5
    },
    "tower_shield": {
        "name": "Tower Shield",
        "type": "shield",
        "attack": 0,
        "defense": 7
    },
    "runic_shield": {
        "name": "Runic Shield",
        "type": "shield",
        "attack": 0,
        "defense": 8
    },
    "diamond_shield": {
        "name": "Diamond Shield",
        "type": "shield",
        "attack": 0,
        "defense": 10
    },
    "kings_shield": {
        "name": "King's Shield",
        "type": "shield",
        "attack": 0,
        "defense": 12
    }
}


def choose_action():
    while True:
        choice = input("Choose: ").strip()
        if choice in ("1", "2"):
            return choice
        print("Invalid input")


def open_chest(character):
    # Better equipment becomes more likely as rooms are completed.
    # Both equipment slots always have the same total chance.
    target_tier = min(7, character["rooms_explored"] / 8)
    item_names = list(chest_items)
    weights = [
        1 / (1 + abs((index % 8) - target_tier)) ** 3
        for index in range(len(item_names))
    ]
    item_name = random.choices(item_names, weights=weights, k=1)[0]
    found_item = chest_items[item_name]
    inventory.offer_equipment(character, found_item)
    character["rooms_explored"] += 1


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
            character["hp"] -= 5
            print("You got hit on the way out and lost 10 HP!")
            print()
            print("You have " + str(character["hp"]) + " left")

    elif event == "spawn_chest":
        print("You have found a chest!")
        print("1) Open")
        print("2) Leave")
        choice = choose_action()
        if choice == "1":
            open_chest(character)
