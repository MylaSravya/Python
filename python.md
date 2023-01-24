## 1) What is Python?
Python is an interpreted high-level, general-purpose programming language. We can build almost any type of application using Python with third-party libraries and frameworks. Python is one of the most popular programming languages in advanced technologies like AI, Data Science, etc.

## 2) What is the main difference between an interpreter and a compiler?
The interpreter translates one statement at a time into machine code, whereas the compiler translates the entire code at a time into machine code.

## 3) Is Python statically typed or dynamically typed language?
Python is a dynamically typed language.

## 4) What do you mean by dynamically typed language?
Dynamically typed languages check the types of variables at run-time. Some dynamically typed languages are Python, JavaScript, Ruby, etc.

**Bonus:** Statically typed languages check the types of variables at compile-time. Some statically typed languages are C++, C, Java, etc..,

## 5) Give some applications of Python.
Python has simpler and easy-to-learn syntax. It may look similar to English. The community of developers for Python is huge. We can find many third-party packages to work with different types of application development. When it comes to development, we can create web applications, GUI applications, CLI applications, etc..,

One of the most popular applications of Python is automation. We can easily create scripts in Python to automate tasks like cleaning disk, send mails, getting data about product prices, etc..,. Python is one of the most popular languages to use in the field of Data Science.

## 6) What applications did you build using Python?
I have written multiple automation scripts to eliminate repetitive and boring tasks. And scripts to get info about product prices, availability, etc.

I have also worked with the frameworks like Django, Flask to build web applications. And build some web applications using both Django and Flask.

## 7) What are the built-in data types in Python?
There are multiples built-in data types in Python. They are int,  float, complex, bool, list, tuple, set, dict, str.

## 8) What’s the difference between list and tuple?

Both list and tuple are used to store the collection of objects. The main difference between the list and tuple is “the list is mutable object whereas tuple is an immutable object”.

## 9) What are mutable and immutable data types?
Mutable data types can be changed after creating them. Some of the mutable objects in Python are list, set, dict.

Immutable data types can’t be changed after creating them. Some of the immutable objects in Python are str, tuple.

## 10() Explain some methods of the list.
* 1. append – the method is used to add an element to the list. It adds the element to the end of the list.
```python
a = [1, 2]
a.append(3)
a
#[1, 2, 3]
```
* 2. pop – the method is used to remove an element from the list. It will remove the last element if we don’t provide any index as an argument or remove the element at the index if we provide an argument.
```python
a = [1, 2, 3, 4, 5]
a.pop()
#5
a
#[1, 2, 3, 4]
a.pop(1)
#2
a
#[1, 3, 4]
```
* 3. remove – the method is used to remove an element from the list. We need to provide the element as an argument that we want to remove from the list. It removes the first occurrence of the element from the list.
```python
a = [1, 2, 2, 3, 4]
a = [1, 2, 3, 2, 4]
a.remove(1)
a
#[2, 3, 2, 4]
a.remove(2)
a
#[3, 2, 4]
```
* 4. sort – the method used to sort the list in ascending or descending order.
```python
a = [3, 2, 4, 1]
a.sort()
a
#[1, 2, 3, 4]
a.sort(reverse=True)
a
#[4, 3, 2, 1]
```
* 5. reverse – the method is used to reverse the list elements.
```python
a = [3, 2, 4, 1]
a.reverse()
a
#[1, 4, 2, 3]
```
Note: There are other methods like clear, insert, count, etc… You don’t have to explain every method of the list to the interviewer. Just explain two or three methods that you mostly use.

## 11) Explain some methods of string
* 1. split – the method is used to split the string at desired points. It returns the list as a result. By default, it splits the string at spaces. We can provide the delimiter as an argument for the method.
```python
a = "This is Geekflare"
a.split()
#['This', 'is', 'Geekflare']
a = "1, 2, 3, 4, 5, 6"
a.split(", ")
#['1', '2', '3', '4', '5', '6']
```
* 2. join – the method is used to combine the list of string objects. It combines the string objects with the delimiter we provide.
```python
a = ['This', 'is', 'Geekflare']
' '.join(a)

#'This is Geekflare'
#', '.join(a)
#'This, is, Geekflare'
```
Note: Some other methods of strings are: capitalize, isalnum, isalpha, isdigit, lower, upper, center, etc..,

## 12) What’s the negative indexing in lists?
The index is used to access the element from the lists. Normal indexing of the list starts from 0.

Similar to normal indexing, negative indexing is also used to access the elements from the lists. But, negative indexing allows us to access the index from the end of the list. The start of the negative indexing is -1. And it keeps on increasing like -2, -3, -4, etc.., till the length of the list.
```python

a = [1, 2, 3, 4, 5]
a[-1]
#5
a[-3]
#3
a[-5]
#1
```
## 13) Explain some methods of dict
* 1. items – the method returns key: value pairs of dictionaries as a list of tuples.
```python
a = {1: 'Geekflare', 2: 'Geekflare Tools', 3: 'Geekflare Online Compiler'}
a.items()
#dict_items([(1, 'Geekflare'), (2, 'Geekflare Tools'), (3, 'Geekflare Online Compiler')])
```
* 2. pop – the method is used to remove the key: value pair from the dictionary. It accepts the key as an argument and removes it from the dictionary.
```python
a = {1: 2, 2: 3}
a.pop(2)
#3
a
#{1: 2}
Note: Some other methods of dict are: get, keys, values, clear, etc.
```
## 14) What is slicing in Python?
Slicing is used to access the subarray from a sequence data type. It returns the data from the sequence data type based on the arguments we provide. It returns the same data type as the source data type.

**Slicing accepts three arguments.** They are the start index, end index, and increment step. The syntax of slicing is variable[start:end:step]. Arguments are not mandatory for slicing. You can specify an empty colon (:) which returns the entire data as the result.
```python
a = [1, 2, 3, 4, 5]
a[:]
#[1, 2, 3, 4, 5]
a[:3]
#[1, 2, 3]
a[3:]
#[4, 5]
a[0:5:2]
#[1, 3, 5]
```
## 15) Which data types allow slicing?
We can use slicing on list, tuple, and str data types.

## 16) What are unpacking operators in Python? How to use them?
* The * and ** operators are unpacking operators in Python.
* The * unpacking operator is used to assign multiple values to different values at a time from sequence data types.
```python
items = [1, 2, 3]
a, b, c = items
a
#1
b
#2
c
#3
a, *b = items
a
#1
b
#[2, 3]
* The ** unpacking operator is used with dict data types. The unpacking in dictionaries doesn’t work like unpacking with sequence data types.
* The unpacking in dictionaries is mostly used to copy key: value items from one dictionary to another.
```python
a = {1:2, 3:4}
b = {**a}
b
#{1: 2, 3: 4}
c = {3:5, 5:6}
b = {**a, **c}
b
#{1: 2, 3: 5, 5: 6}
Note: You can refer to this article for more info on these operators.
```
## 17) Does Python have switch statements?
No, Python doesn’t have switch statements.

## 18) How do you implement the functionality of switch statements in Python?
We can implement the functionality of switch statements using if and elif statements.
```python
if a == 1:
    print(...)
elif a == 2:
    print(....)
```

## 19) What are break and continue statements?
**break ** – the break statement is used to terminate the running loop. The execution of the code will jump to the outside of the break loop.
```python
for i in range(5):
    if i == 3:
        break
print(i)

# 0
# 1
# 2
```
**continue** – the continue statement is used to skip the execution of the remaining code. The code after the continue statement doesn’t execute in the current iteration, and the execution goes to the next iteration.
```python

for i in range(5):
    if i == 3:
        continue
print(i)

# 0
# 1
# 2
# 4
```

## 20) When is the code in else executed with while and for loops?
The code inside the else block with while and for loops is executed after executing all iterations. And the code inside the else block doesn’t execute when we break the loops.

## 21) What are list and dictionary comprehensions?
List and dictionary comprehensions are syntactic sugar for the for-loops.
```python
a = [i for i in range(10)]
a
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = {i: i + 1 for i in range(10)}
a
#{0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}
```

## 22) How does the range function work?
The range function returns the sequence of numbers between the start to stop with a step increment. The syntax of the range function is range(start, stop[, step]).

The stop argument is mandatory. The arguments start and step are optional. The default value of start and step are 0 and 1, respectively.
```python

list(range(10))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 10))
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 10, 2))
#[1, 3, 5, 7, 9]
```

## 23) What are the parameters and arguments?
*Parameters are the names listed in the function definition.
*Arguments are the values passed to the function while invoking.

## 24) What are the different types of arguments in Python?
There are mainly four types of arguments. They are positional arguments, default arguments, keyword arguments, and arbitrary arguments.

* **Positional Arguments:** the normal arguments that we define in user-defined functions are called positional arguments. All positional arguments are required while invoking the function.
```python
def add(a, b):
    return a + b
add(1, 2)
#3
add(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: add() missing 1 required positional argument: 'b'

```
**Default Arguments:** we can provide the value to the arguments in the function definition itself as default value. When the user didn’t pass the value, the function will consider the default value.
```python
def add(a, b=3):
    return a + b
add(1, 2)
#3
add(1)
#4
```
**Keyword Arguments:** we can specify the name of the arguments while invoking the function and assign values to them. The keyword arguments help us to avoid ordering which is mandatory in positional arguments.
```python
def add(a, b):
    print("a ", a)
    print("b ", b)
    return a + b
add(b=4, a=2)

# 2
# 4
# 6
```

**Arbitrary Arguments:** we use arbitrary arguments to collect a bunch of values at a time when we don’t know the number of arguments that function will get. We * and ** operators in the function definition to collect the arguments.
```python
def add(*args):
    return sum(args)
add(1, 2, 3, 4, 5)
#15
def dict_args(**kwargs):
    print(kwargs)

# dict_args(a='Geekflare', b='Geekflare Tools', c='Geekflare Online Compiler')
# {'a': 'Geekflare', 'b': 'Geekflare Tools', 'c': 'Geekflare Online Compiler'}
```

## 25) What is the lambda function?
Lambda functions are small anonymous functions in Python. It has single expressions and accepts multiples arguments.
```python
add = lambda a, b: a + b
add(1, 3)
#4
```
## 26) What’s the difference between normal function and lambda function?
The functionality of both normal functions and lambda functions are similar. But, we need to write some extra code in normal functions compared to lambda functions for the same functionality. Lambda functions come in handy when there is a single expression.

## 27) What is the pass keyword used for?
The pass keyword is used to mention an empty block in the code. Python doesn’t allow us to leave the blocks without any code. So, the pass statement allows us to define empty blocks (when we decide to fill the code later).
```python
def add(*args):

  File "<stdin>", line 3
    ^
# IndentationError: expected an indented block
# def add(*args):
# ...     pass
```

## 28) What is a recursive function?
The function calling itself is called a recursive function.

## 29) What are packing operators in Python? How to use them?
The packing operators are used to collect multiple arguments in functions. They are known as arbitrary arguments.

Note: you can refer to this article for more info on packing operators in Python.

## 30) OOPs in Python
What keyword is used to create classes in Python?
The class keyword is used to create classes in Python. We should follow the pascal case for naming the classes in Python as an industry-standard practice.
```python
class Car:
    pass
```
##31) How to instantiate a class in Python?
We can create an instance of a class in Python by simply calling it like function. We can pass the required attributes for the object in the same way as we do for function arguments.
```python
class Car:
    def __init__(self, color):
        self.color = color
red_car = Car('red')
red_car.color
#'red'
green_car = Car('green')
green_car.color
#'green'
```
## 32) What is self in Python?
The self represents the object of the class. It’s used to access the object attributes and methods inside the class for the particular object.

## 33) What is the __init__ method?
The __init__ is the constructor method similar to the constructors in other OOP languages. It executes immediately when we create an object for the class. It’s used to initialize the initial data for the instance.

## 34) What is docstring in Python?
The documentation strings or docstrings are used to document a code block. They are also used as multi-line comments.

These docstrings are used in the methods of a class to describe what a certain method does. And we can see the method docstring using the help method.
```python
class Car:
    def __init__(self, color):
        self.color = color
    def change_color(self, updated_color):
        """This method changes the color of the car"""
        self.color = updated_color
car = Car('red')
help(car.change_color)
Help on method change_color in module __main__:

change_color(updated_color) method of __main__.Car instance
    This method changes the color of the car

```
## 35) What are dunder or magic methods?
The methods having two prefix and suffix underscores are called dunder or magic methods. They are mainly used to override the methods. Some of methods that we can override in classes are __str__, __len__, __setitem__, __getitem__, etc..,
```python
class Car:
    def __str__(self):
        return "This is a Car class"
car = Car()
print(car)
#This is a Car class
```
**Note:** There are a lot of other methods that you can override. They come in handy when you want to customize the code in depth. Explore the documentation for more info.

## 36) How do you implement inheritance in Python?
We can pass the parent class to the child class as an argument. And we can invoke the init method parent class in the child class.
```python
class Animal:
    def __init__(self, name):
        self.name = name
class Animal:             e):
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)

class Dog(Animal):        e):ame)
def __init__(self, name):
    super().__init__(name)
doggy = Dog('Tommy')
doggy.display()

#Tommy
```

## 37) How to access parent class inside child class in Python?
We can use the super() which refers to the parent class inside the child class. And we can access attributes and methods with it.

## 38) How to use single-line and multi-line comments in Python?
We use hash (#) for single-line comments. And triple single quotes (”’comment”’) or triple double quotes (“””comment”””) for multi-line comments.

## 39) What is an object in Python?
Everything in Python is an object. All the data types, functions, and classes are objects.

## 40) What is the difference between is and ==?
The == operator is used to check whether two objects have the same value or not. The is operator is used to check whether two objects are referring to the same memory location or not.
```python
a = []
b = []
c = a
a == b
#True
a is b
#False
a is c
#True
```
## 41) What is shallow and deep copy?
Shallow Copy: it creates the exact copy as the original without changing references of the objects. Now, both copied and original objects refer to the same object references. So, changing one object will affect the other.

The copy method from the copy module is used for the shallow copy.
```python
from copy import copy
a = [1, [2, 3]]
b = copy(a)
a[1].append(4)
a
#[1, [2, 3, 4]]
b
#[1, [2, 3, 4]]
```
**Deep Copy:** it copies the values of the original object recursively into the new object. We have to use the slicing or deepcopy function from the copy module for the deep copying.
```python

from copy import deepcopy
a = [1, [2, 3]]
b = deepcopy(a)
a[1].append(4)
a
#[1, [2, 3, 4]]
b
#[1, [2, 3]]
b[1].append(5)
a
#[1, [2, 3, 4]]
b
#[1, [2, 3, 5]]
```

##42) What are iterators?
Iterators are objects in Python which remember their state of iteration. It initializes the data with the __iter__ method and returns the next element using the __next__ method.

We need to call the next(iterator) to get the next element from the iterator. And we can convert a sequence data type to an iterator using the iter built-in method.
```python
a = [1, 2]
iterator = iter(a)
next(iterator)
next(iterator)
next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

## 43) What are generators?
Generators are the functions that return an iterator like a generator object. It uses the yield to generate the data.

```python
def numbers(n):
    for i in range(1, n + 1):
        yield i
        _10 = numbers(10)
        next(_10)
        next(_10)
        next(_10)
        next(_10)
```