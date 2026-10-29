import random

import combat
import inventory

events = ("spawn_monster", "spawn_chest")

chest_items = {
    # Swords
    "rusty_sword": {
        "name": "Rusty Sword",
        "type": "weapon",
        "attack": 3,
        "defense": 0
    },
    "wooden_sword": {
        "name": "Wooden Sword",
        "type": "weapon",
        "attack": 5,
        "defense": 0
    },
    "iron_sword": {
        "name": "Iron Sword",
        "type": "weapon",
        "attack": 10,
        "defense": 0
    },
    "steel_sword": {
        "name": "Steel Sword",
        "type": "weapon",
        "attack": 15,
        "defense": 0
    },
    "knights_sword": {
        "name": "Knight's Sword",
        "type": "weapon",
        "attack": 20,
        "defense": 0
    },
    "diamond_sword": {
        "name": "Diamond Sword",
        "type": "weapon",
        "attack": 25,
        "defense": 0
    },
    "flame_sword": {
        "name": "Flame Sword",
        "type": "weapon",
        "attack": 30,
        "defense": 0
    },
    "kings_sword": {
        "name": "King's Sword",
        "type": "weapon",
        "attack": 40,
        "defense": 0
    },

    # Shields
    "broken_shield": {
        "name": "Broken Shield",
        "type": "shield",
        "attack": 0,
        "defense": 2
    },
    "wooden_shield": {
        "name": "Wooden Shield",
        "type": "shield",
        "attack": 0,
        "defense": 5
    },
    "iron_shield": {
        "name": "Iron Shield",
        "type": "shield",
        "attack": 0,
        "defense": 10
    },
    "steel_shield": {
        "name": "Steel Shield",
        "type": "shield",
        "attack": 0,
        "defense": 15
    },
    "tower_shield": {
        "name": "Tower Shield",
        "type": "shield",
        "attack": 0,
        "defense": 20
    },
    "runic_shield": {
        "name": "Runic Shield",
        "type": "shield",
        "attack": 0,
        "defense": 25
    },
    "diamond_shield": {
        "name": "Diamond Shield",
        "type": "shield",
        "attack": 0,
        "defense": 35
    },
    "kings_shield": {
        "name": "King's Shield",
        "type": "shield",
        "attack": 0,
        "defense": 40
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
            print("You have escaped")
    elif event == "spawn_chest":
        print("You have found a chest!")
        print("1) Open")
        print("2) Leave")
        choice = choose_action()
        if choice == "1":
            open_chest(character)
