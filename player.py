def create_character():
    name = input("Enter new character name: ")
    if name in characters["name"]:
        print("Name already in use, try a different one")
        create_character()
    else:
        characters["name"] = name


characters = {
    {
        "character" : {
            "name" : create_character(),
            "attack" : 20,
            "defense" : 10,
            "hp" : 100,
    }
    
}
}
