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

'''
types = {
    "Electric": [],
    "Fire": [],
    "Grass": []
}


types["Electric"].append("Pikachu")
types["Fire"].append("Scovillain")
types["Fire"].append("Charmander")
types["Grass"].append("Bulbausau")
types["Grass"].append("Scovillain")
types["Grass"].append("Leafeaon")

print(types)


for k in types.keys():
    print(k)


print("=====================")
for k in types.keys():
    if k == "Grass" or k == "Fire":
        continue
    print(k)

'''

#1.8 / 1.9 / 1.10

'''
superheroes = {
    " Batman " : {
    " id " : 1 ,
    " aliases " : [ " Bruce Wayne " , " Dark knight "],
    " location " : {
        " number " : 1007 ,
        " street " : " Mountain Drive " ,
        " city " : " Gotham "
        }
    },
    " Superman " : {
    " id " : 2 ,
    " aliases " : [ " Kal - El " , " Clark Kent " , " The Man of Steel " ],
    " location " : {
        " number " : 344 ,
        " street " : " Clinton Street " ,
        " apartment " : " 3 D " ,
        " city " : " Metropolis "
        }
    },

}

superheroes[" Batman "][" aliases "].append("Caped Crusader")
#print(superheroes)

superheroes["Wolverine"] = {"id": 3, " aliases ": []}

#print(superheroes)

for i in superheroes :
    print(f'{i} : ')
    for j in superheroes[i][" aliases "]:
        if i == "Wolverine":
            print("No alias found")
        print(j)


'''

'''
values = {
    " dalmatians " : 101 ,
    " pi " : 3.14 ,
    " beast " : 666 ,
    " life " : 42 ,
    " googol ": 10**100 ,
    " jordan ": 23 ,
    " life , the universe and everything " : 42 ,
    " emergency " : 911 ,
    " euler " : 2.71828
}

max = ''
for i in values:
    if values[i] > max:
        max == i

print(max)
'''

#Challenge

'''
one = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"]

two = ["D", "G"]

three = ["B", "C", "M", "P"]

four = ["F", "H", "V", "W", "Y"]

five = ["K"]

eight = ["J", "X"]

ten = ["Q", "Z"]

essai = input("Entrez un mot : ")

points = 0

for letter in essai:
    if letter.capitalize() in one:
        points += 1
    elif letter.capitalize() in two:
        points += 2
    elif letter.capitalize() in three:
        points += 3
    
    elif letter.capitalize() in four:
        points += 4

    elif letter.capitalize() in five:
        points += 5
    
    elif letter.capitalize() in eight:
        points += 8
    
    elif letter.capitalize() in ten:
        points += 10

print(points)
'''


#2.1 / 2.2

'''
is_sunny = True

is_raining = False

print(is_raining, is_sunny)


is_sunny = True

is_raining = not is_sunny

print(is_raining, is_sunny)

'''

#2.3

listes = {
    "l1" : [ True , True ],
    "l2" : [ False , False ],
    "l3" : [ True , False ],
    "l4" : [ False , True ]
}

for k, v in listes.items():
    if v[0] and v[1] :
        print(f"{k} : Both are True")
    if v[0] or v[1] :
        print(f"{k} : At least one is True")
    
    else : 
        print(f"{k} : None are True")