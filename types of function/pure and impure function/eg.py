'''
pure and impure function
PURE :
In pure function , it does not affect the anything outside the funuction
IMPURE:
In impure function,,it does afect the code(it can variable or other function)
'''

# eg impure function
total=10

def add(amount):
    global total
    total+=amount
    print("I am from the add func",total)

def summa():
    print ("I am from the summa func",total)

add(20)
summa()

# pure function

total=10

def add(amount):
    total = 0
    total+=amount
    print("I am from the add func",total)

def summa():
    print ("I am from the summa func",total)

add(20)
summa()