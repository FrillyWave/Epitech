#1.1

'''
def f1():
    return 42

def f2(x):
    return 2 * x

print ( f1 () )
print ( f2 (5) + f1 () )
'''


#1.2


'''
def bread () :
    print (" <////////// > " )
def lettuce () :
    print (" ~~~~~~~~~~~~ " )
def tomato () :
    print (" O O O O O O " )
def ham () :
    print (" ============ " )
'''

'''
bread()
lettuce()
tomato()
ham()
ham()
bread()
'''

#1.3
'''
for i in range(4):
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()
'''

#1.4

'''
def make_burger(n):
    if not type(n) == int :
        return "N must be an integer"
    for i in range(n):
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()

print(make_burger(8))
'''

#1.5

'''
def make_burger(n):
    vegan = False
    sans_viande = input("Burger végan ?")
    if sans_viande in ["oui", "yes", "yeah"]:
        vegan = True
        for i in range(n):
            bread()
            lettuce()
            tomato()
            lettuce()
            tomato()
            bread()
    else : 
        for i in range(n):
            bread()
            lettuce()
            tomato()
            ham()
            ham()
            bread()

print(make_burger(4))
'''


#Challenge
'''
import time
def power(a, b):
    return a ** b

start = time.time()
print(power(42, 84))
duree = time.time() - start
print(duree)
'''
'''
start = time.time()
print(power(42, 168))
duree = time.time() - start
print(duree)

start = time.time()
print(power(42, 288))
duree = time.time() - start
print(duree)
'''

#2.1
'''
def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

print(sum(42))
'''

#2.2
'''
def palindrome():
    t = input("ENtrez une chaine : ")
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    t = t.lower()
    new_t = ""
    for letter in t:
        if letter in letters:
            new_t = new_t + letter
    reversed_t = new_t[::-1]
    if new_t == reversed_t:
        print("It's a palindrome")
    else :
        print("no")

palindrome()
'''

#2.3
'''
import os 
def ls_r(path):
    entries = os.listdir(path)
    entries.reverse()  # Reverse the order
    for entry in entries:
        print(entry)
ls_r(".")
'''

#3.1


def funA(s, n):
    length = len(s)
    if length < n:
        print("trop petit")
        return False
    else :
        print("ok")
        return True

#funA("Bonjourrsgdsg", 8)

def funB(s, n):
    special = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    cpt = 0
    for letter in s:
        if letter in special:
            cpt += 1
    if cpt < n :
        print(f"Le mdp doit contenir au moins {n} caractères spéciaux. Vous n'en avez que {cpt}")
        return False
    else : 
        print(f"ok. Vous avez {cpt} caractères spéciaux")
        return True

#funB("Bonjour!'(è-)", 8)

def funC(s, n):
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cpt = 0
    for char in s:
        if char in num:
            cpt += 1
    if cpt < n :
        print(f"Le mdp doit contenir au moins {n} chiffres. Vous n'en avez que {cpt}")
        return False
    else:
        print(f"Ok. Vous avez {cpt} chiffres")
        return True
    
#funC("hello84268", 4)

#3.2 / 3.3

def passcheck(func, n, s):
    try :
        if func == "funA":
            funA(s, n)
        if func == "funB":
            funB(s, n)
        if func == "funC":
            funC(s, n)
    except SyntaxError as e:
        print(f"Il y a une erreur {e}")

passcheck("funA", 16, "mysecretpassword" )
passcheck("funB", 3, "mysecretpassword" )
passcheck("funC", 1, "mysecretpassword"  )
