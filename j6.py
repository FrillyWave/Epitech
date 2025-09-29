#1.1 / 1.2 

'''
pokemon = {
    "Pikachu" : "Electic",
    "Bulbausaur": "Grass",
    "Charmander": "Fire"
}

pokemon["Blaziken"] = "Fire"

print(pokemon)
'''


#1.3

"""
pokemon = {
    "Pikachu" : "Electic",
    "Bulbausaur": "Grass",
    "Charmander": "Fire"
}

pokemon["Pikachu"] = ["Pichu", "Raichu"]

print(pokemon)
"""

#We see that the value of pikachu is replaced by the new value


#1.4 / 1.5 / 1.6


types = {
    "Electric": [],
    "Fire": [],
    "Grass": []
}

'''
types["Electric"].append("Pikachu")
types["Fire"].append("Scovillain")
types["Fire"].append("Charmander")
types["Grass"].append("Bulbausau")
types["Grass"].append("Scovillain")
types["Grass"].append("Leafeaon")

print(types)
'''

for k in types.keys():
    print(k)


print("=====================")
for k in types.keys():
    if k == "Grass" or k == "Fire":
        continue
    print(k)