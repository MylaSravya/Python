class private_test():

    __private_var1 = "This is a Private Value"
    public_var = "This is a public value"


# Create an object of the provate_test class
ObjPrv = private_test()
print(ObjPrv.public_var)
print(ObjPrv.__private_var1)