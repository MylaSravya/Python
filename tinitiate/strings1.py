"""
var_test_string = "Python is cool"
print(var_test_string)

print(var_test_string[0:3])
print(var_test_string[4])

print(var_test_string[10:])

a = 'test'
print('test'.find('e'))
print(a.find('z'))
"""

email="aaa.bbb.1@gmail.com"
#email="aaa_sssssbbb@googlemail.com"
#email="a.n.a.bbb.1@yahoo.co.in"

print(email.find('@'))
cleaned_str =email[email.find('@'):]
print(cleaned_str)
dot_pos=cleaned_str.find('.')
print(cleaned_str[1:dot_pos])




