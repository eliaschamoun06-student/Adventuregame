import random

enemies = {
    "goblin": {
        "hp": 100,
        "attack": 10,
        "defense": 10
    },
    "spider": {
        "hp": 60,
        "attack": 15,
        "defense": 5
    },
    "skeleton": {
        "hp": 80,
        "attack": 20,
        "defense": 10
    },
    "troll": {
        "hp": 150,
        "attack": 25,
        "defense": 15
    },
    "slime": {
        "hp": 120,
        "attack": 8,
        "defense": 2
    },
    "giant rat": {
        "hp": 40,
        "attack": 12,
        "defense": 2
    },
    "wolf": {
        "hp": 70,
        "attack": 22,
        "defense": 5
    },
    "orc": {
        "hp": 110,
        "attack": 23,
        "defense": 12
    },
    "zombie": {
        "hp": 140,
        "attack": 12,
        "defense": 5
    },
    "ghost": {
        "hp": 45,
        "attack": 28,
        "defense": 3
    },
    "stone golem": {
        "hp": 160,
        "attack": 15,
        "defense": 18
    },
    "dark knight": {
        "hp": 90,
        "attack": 25,
        "defense": 16
    }
}

def create_monster(monster_type, rooms_explored):
    monster = enemies[monster_type].copy()

    multiplier = rooms_explored * 0.05 + 1

    monster["name"] = monster_type
    monster["hp"] = round(monster["hp"] * multiplier)
    monster["attack"] = round(monster["attack"] * multiplier)
    monster["defense"] = round(monster["defense"] * multiplier)

    return monster

def random_monster(rooms_explored):
    monster_type = random.choice(list(enemies))
    return create_monster(monster_type, rooms_explored)
