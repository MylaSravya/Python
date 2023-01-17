# LISTS
"""
a = 1 # Value

a1 = [77,44,33,22] # empty list value

a1.append(12)
a1.append(14)

# [12, 14]
print(a1)
print(a1[0])
print(a1[3])
# [77, 44, 33, 22, 12, 14]
print(a1[2:5])

CompoundList = [1, 100.55, 'a', 'ZZ']
print (CompoundList)

a1.insert(2,99)
print(a1)

a1[3]=100
print(a1)
"""

a1 = [77, 44, 33, 22, 12, 14]
print(len(a1))   # OUTPUT: 5
print(len([1, 2, 3])) # OUTPUT: 3

# get Min and Max element in the list
print(min(a1))  # OUTPUT: 1
print(max(a1))  # OUTPUT: 5
print(sum(a1))  # OUTPUT: 19

# Sort a list
# -----------
a1.sort()
print(a1)  # OUTPUT: [1, 2, 3, 4, 4, 5]a1
a1.reverse()
print(a1)

str_list = ["dog","Cat","cat","pig","eel"]
print(min(str_list)) 