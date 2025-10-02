#1.1

def sum(*args):
    total = 0
    for arg in args:
        try : 
            total += arg
        except TypeError as e:
            print("Args must be numbers")
    print(total)

#sum(1)
#sum(1, 2, 3)
#sum(-20, -10, 5, 5, 10, 10)
#sum("toto", 1)
 

#1.2

 

def my_division(a, b):
    try : 
        print(a // b)
        print(a % b)
    except ZeroDivisionError as e:
        print(f"Fatal error : We can't divide by zero")

#my_division(42, 0)
 

#1.3

 
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

#my_count(8, 3) #Print too many numbers, I don't know why
 

#1.4 (not possible until 1.3 is fixed)

#1.5

 
def new_division(num, den, acc=1):
    try :
        res = (num / den)
        print(round(res, acc))
    except ZeroDivisionError as e:
        print(f"Fatal error : We can't divide by zero")
    except TypeError as e:
        print("Args must be numbers")


#new_division(8, 3, 5)
#new_division(7, 3)
#new_division(32, 3, "toto")
 

#1.6


 
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

#ship("Superman", "The man of steel", apartment="3D", num= 344, street="Clinton Street", city="Metropolis")
 

#Challenge (undone)

 
def count_letter(n):
    if not isinstance(n, int):
        print("Error : Argument must be a integer")
        return
 


#2.1
 
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.readlines()
        print(content)
    
#read_file("j9/primes.txt")
 
#2.2
 
def read_line(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)

    except FileNotFoundError as e:
        print(f"Error : The file {file_name} was not found.")

#read_file("j9/zen.txt")
 

#2.3
 
def read_lines(file_name, line_number):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if line_number < 1 or line_number > len(lines):
                print("Error : Line number out of range.")
                return
            print(lines[line_number - 1].rstrip())

    except FileNotFoundError as e:
        print(f"Error : The file {file_name} was not found.")


#read_lines("j9/primes.txt", 3)
#read_lines("j9/primes.txt", 300)
 

#2.4

 
def count_lines(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(len(lines))

#count_lines("j9/primes.txt")
#count_lines("j9/zen.txt")
 

#2.5


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("")

#create_file("j9/toto.txt")


#2.6

def write(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)

#write("j9/toto.txt", "I'm a new line")

#2.7


def rewrite(file, file_to_copy):
    #Opening the file to copy in read mode and the target file in write mode
    with open(file_to_copy, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

rewrite("j9/toto.txt", "j9/zen.txt")


#2.8
def longest(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    longest_word = ""
    words = content.split()
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"{longest_word} : {len(longest_word)}")

#longest("j9/zen.txt")

#2.9

def frequency_word():
    with open("j9/zen.txt", 'r', encoding='utf-8') as f:
        content = f.read().lower()

    words = content.split()
    frequency = {}
    for word in words:
        word = word.strip('.,!?;"()[]{}<>')
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    for word, count in frequency.items():
        print(f"{word} : {count}")

#frequency_word()

#2.10

def frequency_letter():
    with open("j9/zen.txt", 'r', encoding='utf-8') as f:
        content = f.read().lower()

    frequency = {}
    for char in content:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for char, count in frequency.items():
        print(f"{char} : {count}")

frequency_letter()