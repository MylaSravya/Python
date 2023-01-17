"""
var_string_1 = "DOUBLE QUOTES STRING:Welcome to python tutorials by tinitiate.com"

# sample string using SINGLE QUOTES
var_string_2 = 'SINGLE QUOTES STRING: Welcome to python tutorials by tinitiate.com'
"""
# Multi line string using THREE DOUBLE QUOTES
var_string_3 = """THREE DOUBLE QUOTES MULTI LINE STRING: Welcome to python 
tutorials by tinitiate.com,This is a multi line string
as you can see"""

"""
# print the sthe above strings
print(var_string_1)
print(var_string_2)
print(var_string_3)

"""
var_test_string = "Python is cool"

print(var_test_string[0])
print("Python is cool"[0])
print(var_test_string[-1]);
print(var_test_string[13]);
print(var_test_string[-4])

print(var_test_string[6:])
print(var_test_string[-4:])
print(var_test_string[4:10])
a = "test"
pos = a.find("e")
print(pos)

var_string_case_test = "learn PYTHON"
print(var_string_case_test.upper()) # OUTPUT:  LEARN PYTHON
print(var_string_case_test.lower()) # OUTPUT:  learn python
print(var_string_case_test.title()) # OUTPUT:  Learn Python
print(var_string_case_test.swapcase())  # OUTPUT:  LEARN python
print(var_string_case_test.capitalize())  # OUTPUT:  Learn python
print("learn PYTHON".upper()) # OUTPUT:  Learn Python

print ('test'.rjust(10,'+'))

print ('  '.isspace())
a = True
a = False
b = "True"

print ('test'.center(9,'+'))
print (' This is a test  ')
print (' This is a test  '.strip())


print ('this is a test'.strip('t'))
print ('this is a test this'.lstrip('this'))
print ('this is a test this'.rstrip('this'))
"""
"""



print ('test'.find('t',2)) # print the index of the second occurrence of 't'
# OUTPUT: 3

print ('test'.index('t')) # print the index of the first occurrence of 't'
# OUTPUT: 0
# print ('test'.index('a'))

# Swap values in 2 string variables, without using intermediate variable(s)
A = "ttt"
B = "yyyYa"

# A = "__????"
# B = "[[][][[["

print("Before")
print(A)
print(B)

print(len(A))
A = A + B
print(A)
# print(len(A))
# print(len(B))
B = A[0:len(A)-len(B)]
print(len(B))
print("After")
A = A[len(B):]
print(A)
print(B)

"""