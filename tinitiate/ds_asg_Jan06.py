emp = []
emp.append({'EmpId': 1, 'Ename': 'a', 'Sal': 2000.5}) # , "projects":[11,33,44]})
emp.append({'EmpId': 2, 'Ename': 'b', 'Sal': 1000.5})
emp.append({'EmpId': 3, 'Ename': 'c', 'Sal': 3000.5})

print(emp)
print(emp[2]['Sal'])

# projects=[11,33,44]
# projects=[33,44]
# projects=[11,44,55]

emp[0]['projects']=[11,33,44]
emp[1]['projects']=[33,44]
emp[2]['projects']=[11,44,55]

print(emp)

# print(emp   [2]   ['projects'] [2])
#      list  dict  list         int 

# print(emp)                    # Datatype is list
# print(emp)[2])                # Datatype is dict 
# print(emp)[2]['projects'])    # Datatype is list
# print(emp)[2]['projects'][2]) # Datatype is integer

print(type(emp))                    # Datatype is list
print(type(emp[2]))              # Datatype is dict 
print(type(emp[2]['projects']))  # Datatype is list
print(type(emp[2]['projects'][2])) # Datatype is integer
