from oop_class import oop_demo as c1  # Session, Instance, Copies

f1 = c1()
f2 = c1()

f1.num1 = 100
f1.num2 = 200
a = f1.add1()
print(a)
print(f1.mul1())

f2.num1 = 1000
f2.num2 = 2000
print(f2.add1())
print(f2.mul1())

print(f1.__sizeof__() + f2.__sizeof__())