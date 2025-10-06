#1.1
"""
print(1+1)
print(30+12)
print(777 + (-735))
print(1+2+3+5+7+11+13)
"""

#1.2
"""
print(84<42)
print(0 == -(-(0)))
print(666 != 42)
print(2 ** 21)
print(pow(10,3))
print(9%2)
"""

#1.3
# 84/2 returns a float when 84//2 only returns the quotient so an integer

#1.4
"""
try:
    print(84/(8 + (-3) + (-7) + 2))
except ZeroDivisionError:
    print("On divise pas par zéro")
"""
#2.1 

"""
#print(pow((1 + 11 + 111 + 1111 + 11111 + 111111 + 1111111 + 11111111 + 111111111 + 1111111111), 2))
#print(pow((1 + 11 + 111 + 1111 + 11111 + 111111 + 1111111 + 11111111 + 111111111 + 1111111111), 3))
#print(pow((1 + 11 + 111 + 1111 + 11111 + 111111 + 1111111 + 11111111 + 111111111 + 1111111111), 4))
print(pow((1 + 11 + 111 + 1111 + 11111 + 111111 + 1111111 + 11111111 + 111111111 + 1111111111), 5))
"""

#2.2

#print(17**1024)

#3.1
'''
num = int(input("Enter a number : "))
if num % 2 == 0:
    print("oui")
else :
    print("non")
'''


#3.2

"""
def sum_digits(n):
    x = 0
    for i in str(n):
        x += int(i)
    return x

print(sum_digits(123456789))
print(sum_digits(112233445566778899))
print(sum_digits(123456789 * 987654321))
"""


#3.3 
'''
x = 12.24
x = int(x)
print(x)
'''

'''
x = 424242.8412
x = int(x)
print(x)
'''


#3.4

"""
x = 12.24
x -= int(x)
print(x)
"""

'''
x = 424242.8412
x -= int(x)
print(x)
'''


#4.1

def pi_dec():
    cpt = 0
    dec = 0
    for i in range(1, 10000, 2):
        if cpt % 2 != 0:
            dec -= 1 / i
        else:
            dec += 1 / i
        if i < 10:
            print(dec)
        cpt += 1
    print(dec)
    res = 4 * dec
    pi_dec = res - 3
    return pi_dec

#print(pi_dec())

#4.2

def pi_dec_bis(cpt): 
    if cpt == 900:
        return cpt**2 / 6
    return (cpt * 2 + 1)**2 / (6 + pi_dec_bis(cpt+1))

#print(pi_dec_bis(0)+3)