class xParent():  # Create a Parent Class
    "This is a Parent Class"
    var1 = "Parent-Test"

    def func1(self):
        print("This is parent class")


# Child class that inherits the xParent
# and uses the names same as the ones from the parent class
class xChild(xParent):
    "This is the Child class"
    var1 = "Child-Test"

    def func1(self):
        print("This is child class")

    def func2(self):
        super().func1()

objA = xChild()
objA.func1()  
objA.func2()  