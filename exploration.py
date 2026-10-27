import random
from player import characters

events = {
    "spawn_monster",
    "spawn_chest",
    }

chest_items = {
    "diamond_sword", {
        "damage" : 25,
        "defense" : 10
    },
    "iron_shield", {
        "defense" : 35,
    }
},

def open_chest():
    item = random.choice(list(chest_items))
    if item["damage"] == True:
        print(f"You have found {item}!")
        print("1) Equip")
        print("2) Leave")
        choice = input("Choose: ")
        if choice == 1:
            characters[character["name"]]["attack"] += item["damage"]

def room_event():
    event = random.choice(list(events))
    if event == "spawn_monster":
        print("A monster has appeared")
        print("1) Attack")
        print("2) Escape")
        choice = input("Choose: ")
        if choice == 1:
            print()
        elif choice == 2:
            print("You have escaped")
            return 
    elif event == "spawn_chest":
        print("You have found a chest!")
        print("1) Open")
        print("2) Leave")
        choice = input("Choose: ")
        if choice == 1:
            open_chest()
room_event()