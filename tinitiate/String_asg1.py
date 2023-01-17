"""
print(var_test_string[4:10])
a = "test"
pos = a.find("e")
print(pos)
"""

email = "abc.111.rrrrrr.1@gmail.com"
# email = "abc11@yahoo.co.in"
# email = "aaa.1a_1@hotmail.in"

# print(email.find("@"))
# print(email[email.find("@"):])

cleaned_str = email[email.find("@"):]
print(cleaned_str [1:cleaned_str.find(".") ])
