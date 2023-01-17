"""
for c in range(5):
    print('Loop Count: ',c) # Index starts from ZERO !
    print(c)
    print(c+1)

print("----")

for c in range(4,14):
    print('Loop Count: ',c) # Index starts from ZERO !
    print(c)
    print(c+1)

# LOOP Over the number of characters in a sting
for abc in 'MyString':
    print(abc) # Prints all the characters in new line




# SYNTAX 1: LOOP over elements in a LIST
myList = [1, 2, 3, 4, 5]
#          0  1  2  3  4
#for element in myList:
#    print(element)  # Prints all the elements in new line
"""
myList = [111, 4342, 5653, 334, 115]
#          0    1     2     3    4
# for element in myList:
#    print(element)  # Prints all the elements in new line


# SYNTAX 2: LOOP over elements in a LIST
#for element_index in range(len(myList)):
#    print(myList[element_index])  # Prints all the elements in new line
    # 0  1  2  3  4



# Loop through a sub set of list of elements
for element in myList[2:4]:
    print(element)  # Prints all the elements in new line
"""

for c in range(100):
    if c%2==0:
        print(c)

"""

for outer_loop in range(5):
    for inner_loop in range(5):
        print(outer_loop, '-', inner_loop) 