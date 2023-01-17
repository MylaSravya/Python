
"""
a = 1 # value / data integer
b = a
print(a)
print(b)
print('a')
print("a")
c = "abc" # value string
print(c)
d = 10.3 # value decimals
"""

# List 
emp = [ {"EmpID":1,"Ename":"A","Sal":1000,"Projects":[1,33,44,55]} # 0 dictionary
       ,{"EmpID":2,"Ename":"B","Sal":10000,"Projects":[1,2]}       # 1
       ,{"EmpID":3,"Ename":"C","Sal":3000,"Projects":[33,55]}      # 2
       ,{"EmpID":4,"Ename":"D","Sal":2000,"Projects":[55]}         # 3 
       ]

# print(emp)
print(emp[0]["EmpID"])
print(emp[0]["Projects"][1])
# {"EmpID":1,"Ename":"A","Sal":1000,"Projects":[1,33,44,55]}

print(emp[2]["Sal"])


print(emp[2]["Ename"])

print(emp[0]["Projects"][2])
print(emp[4]["Projects"][2])

# eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}
# print(eats['OKRA'])
"""