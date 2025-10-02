#1.1

"""
num = [-42, 3e2, 666]

max = max(num)
print(max)

print(abs(2))
print(abs(-2))
print(abs(-3e4))
"""


#1.2

'''
print(min('Beautiful is better than ugly'))
'''

#We observe that it doesn't return anything. Min function might be only applyable on a number


#1.3
'''
print(pow(73,73))
'''

#1.4

#The built-in function any() returns True if there is at least one true element in a list.

#The built-in function all() returns True if there is zero false element in a list

'''
liste = [True, False, False, True]

print(any(liste)) #True

print(all(liste)) #False
'''

#1.5

'''

L1 = [1, 2, 3, 4]

L2 = [5, 7, 9, 32]

L3 = [23, 13, 17, 14, 16, 309]

L4 = [10, 20, 30, 40]

print(sum(L1 + L2 + L3 + L4))
'''

#1.6

'''
names = ["Bob", "Emmett", "Gratton", "Mason"]

names.sort(key=len)

print(names) #['Bob', 'Mason', 'Emmett', 'Gratton']

names2 = ["Bob", "Emmett", "Gratton", "Mason"]

names2.sort(key=len, reverse=True)

print(names2) #['Gratton', 'Emmett', 'Mason', 'Bob']
'''

#2.1
'''

crazyFunction = lambda x , y: x * y
meaningOfLife = crazyFunction (6 , 7)
print ( meaningOfLife )

#The output will be 42
'''

#2.2
'''
animalsCounts = [['cat', 666], ['dog', 3], ['elephant', 42]]

sorted = sorted(animalsCounts, key=lambda x: x[1])

print(sorted)
'''

#2.3
'''
print(list(filter(lambda x: x > 10, [3.14, 101, 42, 666, -1]))) #It will create a new list with all elements bigger than 10
'''

#3.1
#print([*enumerate([42, 3, 4, 18, 3, 10])]) #Creates a tuple for each element in the list like following : (index of element, element itself)

#3.2
'''
def check_even(l):
    filtered = list(filter(lambda x: x%2 == 0, l))
    return filtered

print(check_even([1, 2, 3, 4, 5, 6]))
'''

#3.3
'''
words = ['apple', 'banana', 'kiwi', 'pear']

filtered = list(filter(lambda x: len(x) <= 4, words))

print(filtered)
'''

#3.4
'''
celcius = [-10, 0, 17.6, 28, 100]

fahrenheit = list(map(lambda x: (x * 9/ 5) + 32, celcius))

print(fahrenheit)
'''

#3.5

first_names = [ " Jackie " , " Chuck " , " Arnold " , " Sylvester " ]
last_names = [ " Stallone " , " Schwarzenegger " , " Norris " , " Chan "]
magic = [* zip ( first_names , last_names [:: -1]) ]
print ( magic [0])
print ( magic [1][0])
print ( magic [1][1])
print(magic)
#This code creates a list containing tuples with the first name, each one in the order and the last name, in the reversed order. 
#Then, it displays the first element of the new list, the tuple ('Jackie', 'Chan), the first element of the second tuple Chuck and finally the second element of the seconde tuple Norris