class private_test():
    "This is a class to demonstrate the Private variables"
    __private_var1 = "This is a Private Value"
    public_var = "This is a public value"

# Create an object of the provate_test class
ObjPrv = private_test()

# The following code throws an error as the private variable
# is not accessible from outside the class
# print(ObjPrv.__private_var1)
# print the public variable of the class
print(ObjPrv.public_var)