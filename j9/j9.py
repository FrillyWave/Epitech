#1.1
'''
def sum(*args):
    total = 0
    for arg in args:
        try : 
            total += arg
        except TypeError as e:
            print("L'argument doit être un nombre")
    print(total)

#sum(1)
#sum(1, 2, 3)
#sum(-20, -10, 5, 5, 10, 10)
sum("toto", 1)
'''

#1.2

'''

def my_division(a, b):
    try : 
        print(a // b)
        print(a % b)
    except ZeroDivisionError as e:
        print(f"Fatal error : We can't divide by zero")

my_division(42, 0)
'''

#1.3

'''
def my_count(*args):
    if len(args) > 2:
        print("Error : Too many arguments")
        return
    if len(args) == 2 and args[0] > args[1]:
        actual = args[1]
        for i in range(args[1], args[0] + 1):
            print(actual)
            actual += 1
    actual = 0
    for i in range(args[0]):
        print(actual)
        actual += 1

my_count(8, 3) #Print too many numbers, I don't know why
'''

#1.4 (not possible until 1.3 is fixed)

#1.5

'''
def new_division(num, den, acc=1):
    try :
        res = (num / den)
        print(round(res, acc))
    except ZeroDivisionError as e:
        print(f"Fatal error : We can't divide by zero")
    except TypeError as e:
        print("Args must be numbers")


new_division(8, 3, 5)
new_division(7, 3)
new_division(32, 3, "toto")
'''

#1.6


'''
def ship(*name, street=None, city=None, apartment=None, num=None):
    for n in name:
        print(n)
    if street is not None:
        print(f"Street : {street}")
    if apartment is not None:
        print(f"Apartment : {apartment}")
    if city is not None:
        print(f"City : {city}")
    if num is not None:
        print(f"Num : {num}")

#ship("Batman", street="Mountain Drive", city="Gotham")

ship("Superman", "The man of steel", apartment="3D", num= 344, street="Clinton Street", city="Metropolis")
'''

#Challenge (undone)

'''
def count_letter(n):
    if not isinstance(n, int):
        print("Error : Argument must be a integer")
        return
'''

