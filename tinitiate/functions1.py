"""
# Function = method /stored procs
def printme():
    print("Hello")

printme()
printme()
printme()
printme()

def add2nums(n1,n2): # parameters / arguments
    print(n1+n2)

add2nums(n1=10,n2=20)
add2nums(n1=11,n2=22)
add2nums(n1=12,n2=23)
add2nums(12,23)


def addnums(n1,n2): # parameters / arguments
    return n1+n2
    print(123456)

x = addnums(12,23)
print(x)

print(addnums(12,23))

x = addnums(addnums(12,23),addnums(12,23))
print(x)
print(addnums(addnums(12,23),addnums(12,23)))


def even_or_odd(n1):
    if n1%2==0:
        return "even"
        print(123)
    else:
        return "odd"
        print(456)
    print(111)

print(even_or_odd(12))
print(even_or_odd(13))
"""


def add2nums_v2(n1,n2=100):
    print(n1+n2)

add2nums_v2(100)
add2nums_v2(n1=100)
add2nums_v2(n1=200,n2=500)
add2nums_v2(2300,1500)

def arb_args(n1,*n2):
    print(n1)
    print(n2)

arb_args(1,2)
arb_args(1,2,3,4,5)
arb_args(1,2,3,4,5,6,7,8)

def greatest(*a):
    print(max(a))

greatest(11,22,1,3,88,12)
greatest(11,22)
greatest(1133,22222,7)

def print_even(*a):
    x = []
    for n1 in a:
        if n1%2==0:
            x.append(n1)
            # print(n1)
    print(x)        


print_even(11,22,33,44,55)
print_even(11,22)

# Assignment
# print ODD in descending order
def print_odd_desc():
????

print_odd_desc(1,2,33,5,7,6)
print_odd_desc(1,2,33,6,7,8,9,51,12,99)






