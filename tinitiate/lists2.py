
a = 1

a1 = []
a2 = [1,2,3]
a3 = ['a',2,10.2]

# print(a1)
# print(a2)
# print(a3)
# print(a3[2])

print(a1)
a1.append(12)
a1.append(13)
a1.append(11)
a1.append(92)
print(a1)

a1.extend([88,33,44])
print(a1)
# [12, 13, 11, 92, 88, 33, 44]
print(a1[5])

"""
a= [1, [2,3,4], [5,6,7]]
print(a[1][1])

emp = [[1,2,3], ['a','b','c'], [199,333,555]]
print(emp[2][1])
"""

print(a1)
a1.insert(2,99)
print(a1)
a1[3] = 22
print(a1)
# [12, 13, 99, 22, 92, 88, 33, 44]
print(a1[1:4])

a1.sort()
print(a1)
a1.clear()
print(a1)