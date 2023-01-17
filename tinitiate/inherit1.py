class ParentClass():
    
    Parentvar1 = "parentVariable Value"
    
    def parentFunction(self):
        print("This is a message from ParentClass.parentFunction")


#This is a clhld class that inherits ParentClass,
# SYNTAX is to call the parent class as a parameter to the child class
class ChildClass(ParentClass):
    ChildVar1 = "parentVariable Value"
    def childFunction(self):
        print("This is a message from ChildClass.childFunction")


# Create an object of the Child Class
cObj = ChildClass()


# CALL CHILDCLASS and PARENTCLASS methods from the child object
cObj.childFunction()
cObj.parentFunction()
print(cObj.Parentvar1)