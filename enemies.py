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
    }
}

def create_monster(monster_type):
    monster = enemies[monster_type].copy()
    monster["name"] = monster_type
    return monster

def random_monster():
    monster_type = random.choice(list(enemies))
    return create_monster(monster_type)
