"""
myList = [1, 2, 3, 4, 5]
#          0  1  2  3  4
for element in myList:
    print(element)  # Prints all the elements in new line
"""
project_pricing = {1:1000, 2:200, 33:222, 44:51, 55:555}

emp = [ {"EmpID":1,"Ename":"A","Sal":1000,"Projects":[1,33,44,55]} # 0 dictionary
       ,{"EmpID":2,"Ename":"B","Sal":10000,"Projects":[1,2]}       # 1 dictionary 
       ,{"EmpID":3,"Ename":"C","Sal":3000,"Projects":[33,1,55]}      # 2 dictionary
       ,{"EmpID":4,"Ename":"D","Sal":2000,"Projects":[55,2,33]}         # 3 dictionary 
       # ,1                                                          # 4 int
       # ,"aaaa"                                                     # 5 String
       # ,12.222                                                     # 6 Decimal
       # ,[33,44,55]                                                 # 7 List
       # ,(44,55,66)                                                 # 8 Tuple
       ]

# for key, value in project_pricing.items():
#     print(key, value)

"""
for e in emp:
    # print Emps making sal > 2000
    if e["Sal"] > 2000:
        print(e["Ename"])

# Print name of emps working in project 33
for e in emp:
    # print(e["Projects"])
    for project in e["Projects"]:
        if project == 33:
            print(e["Ename"])

"""

# print the name of emp making the highest sal
max_sal = 0
for e in emp:
    if max_sal < e["Sal"]:
        max_sal = e["Sal"]

print(max_sal)
for e in emp:
    if e["Sal"] == max_sal:
        print(e["Ename"])


# print the name of emp making the least sal
min_sal = emp[0]["Sal"]

for e in emp:
    if min_sal > e["Sal"]:
        min_sal = e["Sal"]

print(min_sal)
for e in emp:
    if e["Sal"] == min_sal:
        print(e["Ename"])


# Employee involved in most expensive project totals