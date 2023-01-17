class cons_test():

    # Class Variables
    a = None
    b = None

    # Class Functions / Method
    def adder(self):
        print(self.a + self.b)
        # print(self.d)

    def adder_c(self):
        d = 1
        print(self.a + self.b + self.c)

    def __init__(self,p_a, b, c):
        # Assign to Class variables
        self.a = p_a
        self.b = b

        # Instance Variable
        self.c = c


x = cons_test(12,23,45)
x.adder()
x.adder_c()