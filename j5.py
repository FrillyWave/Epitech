#1.1 

"""
liste = [1, 2, 3, 4, 5]
print(liste[0])
"""

#1.2

"""
liste = [1, 2, 3, 4, 5]
print(liste[-1])
"""


#1.3

'''
liste = []

liste.append(42)
print(liste)

liste.append("forty-two")
print(liste)
'''

#1.4

'''
liste = [1, 2, 3, 4, 5]
print(liste)
for element in liste:
    print(element)
'''

#1.5
"""

liste = [1, 2, 3, 4, 5]
liste.pop()
print(liste)
"""

#1.6

'''
liste = [1, 2, 3, 4, 5]
liste.insert(0, 0)
print(liste)
'''

#1.7

'''
liste = [1, 2, 3, 4, 5]
sub_liste = liste[1:4]
print(sub_liste)
'''

#1.8

'''
liste = [1, 2, 3, 4, 5]
liste.reverse()
print(liste)
'''

#1.9
"""
liste = [1, 2, 3, 4, 5]
new_list = []
for i in range(0, len(liste), 2):
    new_list.append(i)

print(new_list)
"""

#1.10

"""
liste = [1, 2, 3, 4, 5]
i = 11
while i <= 21:
    liste.append(i)
    i += 1

print(liste)
"""

#1.11

#Le code va concatener les deux listes ensemble

#Le deuxième va 


#Challenge

'''
import random
liste = []

for i in range(10000):
    rdm = random.randint(1, 10000)
    liste.append(rdm)

print(liste)

'''

#2.1

student = {
    "name": "Joan",
    "academic_year": 2025,
    "units" : [{"name": "Web dev", "credits": 10, "grade": "A"}, {"name": "Jave", "credits": 5, "grade": "C"}, {"name": "Network", "credits": 2, "grade": "E"}]
}