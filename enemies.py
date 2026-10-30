import random

enemies = {
    "goblin": {
        "hp": 50,
        "attack": 14,
        "defense": 4
    },
    "spider": {
        "hp": 40,
        "attack": 16,
        "defense": 2
    },
    "skeleton": {
        "hp": 55,
        "attack": 15,
        "defense": 4
    },
    "troll": {
        "hp": 75,
        "attack": 16,
        "defense": 5
    },
    "slime": {
        "hp": 65,
        "attack": 12,
        "defense": 2
    },
    "giant rat": {
        "hp": 35,
        "attack": 15,
        "defense": 1
    },
    "wolf": {
        "hp": 45,
        "attack": 17,
        "defense": 2
    },
    "orc": {
        "hp": 60,
        "attack": 16,
        "defense": 4
    },
    "zombie": {
        "hp": 70,
        "attack": 13,
        "defense": 2
    },
    "ghost": {
        "hp": 35,
        "attack": 18,
        "defense": 1
    },
    "stone golem": {
        "hp": 75,
        "attack": 13,
        "defense": 6
    },
    "dark knight": {
        "hp": 60,
        "attack": 16,
        "defense": 5
    }
}

def create_monster(monster_type, rooms_explored):
    monster = enemies[monster_type].copy()

    # Add a fraction of base stats per completed room (not compounded).
    hp_multiplier = 1 + rooms_explored * 0.025
    attack_multiplier = 1 + rooms_explored * 0.025
    defense_multiplier = 1 + rooms_explored * 0.01

    monster["name"] = monster_type
    monster["hp"] = round(monster["hp"] * hp_multiplier)
    monster["attack"] = round(monster["attack"] * attack_multiplier)
    monster["defense"] = round(monster["defense"] * defense_multiplier)

    return monster

def random_monster(rooms_explored):
    monster_type = random.choice(list(enemies))
    return create_monster(monster_type, rooms_explored)
