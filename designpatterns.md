## 1) Define Design Patterns.
Design patterns are known as reusable solutions that help solve commonly recurring issues of software development. Some of these issues are redundant logic and functions, repetitive code, and more. These patterns help save a significant amount of time and effort needed when developing software. Also, these patterns are used commonly in object-oriented software products.

## 2) Can you list some benefits of design patterns?
As mentioned above, these design patterns are flexible enough to identify unwanted repetitive code. With this, the software’s architecture can be customized accordingly. Thus, some of the benefits of design patterns include:

Reusable and can be used in varying projects
Well-tested and effective methods of developing significant solutions
Offer template solutions to define system architecture
Provide utmost transparency to software design

## 3) How can a design pattern be described?

* Define an issue and the corresponding solution
* Finding the variations and language-dependent alternatives for the issue that has to be addressed
* Defining the real-time use cases along with the software’s efficiency.
* To describe a design pattern, the below mentioned things are generally followed:Define a name of the pattern and the classification of the design pattern under which it will fall

## 4) Define the design patterns in Java.
Design Patterns in Java

In Java, there are three varying types of design patterns, such as:

**Creational Patterns:** They offer freedom of choice between the creation of objects by concealing the logic. The constructed objects are decoupled from the implemented system. Some of the examples of this type include abstract factory design, singleton design, prototype design, builder design, and factory design pattern.
**Behavioral Patterns:** These patterns help define how the objects should be communicating and interacting with each other. Strategy pattern, observer patterns, iterator pattern, and command pattern are some examples of behavioral patterns.
**Structural Patterns:** These patterns assist in defining how the structures of objects and classes should look like for defining the composition between objects, interfaces, and classes. Some examples are proxy design, decorator design, facade design, adaptor design, and more.

## 5) What do you mean by Gang of Four (GOF) in design patterns?
Gang of Four (GOF) is used for four authors who invented the concept of design patterns. They are John Vlissides, Richard Hel, Ralph Johnson, and Erich Gamma. They documented the design patterns in the book named “Design Patterns: Elements of Reusable Object-Oriented Software”, which was published in 1995.

## 6) Define some design patterns used in the JDK library of Java.
Some of the design patterns used in the JDK library of Java are:

* Decorator pattern used by the Wrapper classes
* Observer pattern used to handle event frameworks, like swing, AWT, etc.
* Singleton pattern used in classes, like runtime and calendar
* Factory pattern used for methods, like Integer.valueOf methods, etc.

## 7) What do you mean by SOLID principles?
SOLID principles are the object-oriented principles. The SOLID acronym goes:

* S stands for Single Responsibility Principle (SRP): This principle makes sure that every module or class should be responsible for one functionality. And, there should be only one reason to change any class. 
* O stands for Open-Closed Principle (OCP): It says that every class is open for extension and closed for modification. Here, you can extend the behavior of entities by not altering anything available in the existing source code.
* L stands for Liskov Substitution Principle (LSP): The LSP principle talks about objects that can be replaced by subtype instances without impacting the program’s correctness.
* I stands for Interface Segregation Principle (ISP): This one concentrates on the use of as many interfaces specific to the requirements of the client as possible rather than creating a general interface. Herein, clients should not be compelled to integrate the functionalities that they don’t need.
* D stands for Dependency Inversion Principle: Under this principle, the high-level modules shouldn’t be dependent on the concrete implementations or the lower level modules. Rather, they should stay dependent on the abstractions.

## 8) What is the difference between design patterns and design principles?
Design patterns are known as the reusable template solutions used for common issues that can be customized as per the requirements. These can be implemented efficiently, are safe to use and can be tested properly. 

On the other hand, design principles are followed when designing software systems for any sort of platform by using a programming language. The SOLID principles are the design principles that are followed as guidelines to develop extensive, scalable, and robust software systems. These principles can be applied to every aspect of programming. 

## 9) What is the difference between design patterns and algorithms?
Design patterns and algorithms are used to describe typical solutions to a problem. However, the primary difference between these two is that a design pattern offers a high-level description of solutions, and algorithms outline a set of actions to achieve a goal.

## 10) Define Bridge Design Pattern.
The bridge pattern is a structural design pattern type that allows you to split closely related classes or large classes into two hierarchies - implementation and abstraction. These two are independent of one another and can be used whenever you wish to decouple an abstraction from implementation. 

This is known as a bridge pattern as it acts as a bridge between the implementation class and an abstract class. In this pattern, these classes can be modified or altered independently without impacting one another. 

There are four primary elements of bridge pattern, such as:

* **Abstraction:** This is the code and defines the crux of the pattern. It comprises a reference to the implementer.
* **Refined Abstraction:** This is an extension to the abstraction and takes details of the requirements while hiding them from the implementers.
* **Implementer:** This is referred to as the implementation classes’ interface.
* **Concrete Implementation:** This one is the concrete implementation class that integrates the interface of the implementer.

## 11) Explain the Singleton pattern?
Singleton pattern in Java is a pattern which allows a single instance within an application. One good example of the singleton pattern is java.lang.Runtime.

Singleton Pattern states that define a class that has only one instance and provides a global point of access to it. In other words, it is the responsibility of the class that only a single instance should be created, and all other classes can use a single object.

## 12) Describe in how many ways can you create a singleton pattern?
There are two ways of creating a Singleton pattern.

* Early Instantiation - It is responsible for the creation of instance at load time.
* Lazy Instantiation - It is responsible for the creation of instance when required.

## 13) What are the Adapter patterns?
Adapter pattern converts the interface of a class into another interface based on the requirement.

In other words, it let you convert the interface according to requirement while using the class service with a different interface. It is also known as Wrapper.

## 14) Illustrate the uses of Adapter Patterns?
It is used in the following cases:

* When an object requires to utilize an existing class with an incompatible interface.
* In case we want to create a reusable class that collaborates with classes which don't have compatible interfaces.

## 15) Discuss the strategy to describe a design pattern?
The following points should need to be taken care to describe the design pattern.

* The Pattern name and classification.
* The Problem and solution.
* **Consequences:** Variation and language-dependent alternatives should also be addressed.
* **Uses:** Identify the uses in the real systems and its efficiency.

## 16) Difference between Strategy and State design Pattern in Java?
This question is a commonly asked Java design pattern interview question as both Strategy and State pattern has the same structure. The UML class diagram of both patterns looks precisely the same, but their intent is different.

The state design pattern is used to manage and define the state of an object, while the Strategy pattern is used to describe a set of an interchangeable algorithm.

## 17) What are the advantages of Composite design Pattern in Java?
Composite design pattern allows clients to operate collectively on objects that may or may not represent a hierarchy of objects.

Advantage of composite design patterns is as follows.

* It describes the class hierarchy that contains primitive and complex objects.
* It makes it easy to add new kinds of the component.
* It facilitates with the flexibility of structure with a manageable class or interface.

## 18)  Can you describe the uses of the composite pattern?
It is used in the following cases:

* When we want to represent a partial or full hierarchy of objects.
* In case we need to add the responsibilities dynamically to the individual object without affecting other objects.

## 19) What are Some Design Patterns which are used in the JDK library?
Some of the design patterns which are used in the JDK library are as follows.

* The decorator pattern is used by Wrapper classes.
* Singleton pattern is used by Calendar classes (Runtime).
* The Wrapper classes use factory pattern like Integer.valueOf.
* Event handling frameworks use observer pattern like swing, awt.

## 20) Mention advantage of Builder design pattern in Java?
Advantages of builder design patterns are as follows.

* It facilitates with a clear separation between the construction and representation of an object.
* It provides improved control over the construction process.
* The constructor parameter is reduced and is provided in highly readable method calls.
* In design Pattern, the object is always instantiated in a complete state.
* In the Builder design pattern, Immutable objects can be quickly built in the object building process.
  
## 21) Can you write Thread-safe Singleton in Java?
There are many ways to write a Thread-safe singleton in Java.

* Thread-safe Singleton can be written by writing singleton using double-checked locking.
* Another way is, by using static Singleton instance initialized during class loading.
* By using Java enum to create a thread-safe singleton, this is the most straightforward way.

## 22) Is it possible to create a clone of a singleton object?
Yes, it is possible to create a clone of a singleton object.

## 23) What is the proxy pattern, and what does it do?
The term Proxy stands for an object representing another object. The proxy pattern provides a substitute or placeholder for another purpose to control access to it. According to Gangs of four, a Proxy Pattern "provides control for accessing the original object."

We can perform many security operations like hiding the information of the original object, on-demand loading, etc It is also called as placeholder or surrogates.

## 24) Explain some different type of proxies?
There are many cases where the proxy pattern is beneficial. Let's have a look at some different proxies.

**Protection proxy**
It controls access to the real subject based on some condition.

**Virtual proxies**
Virtual proxies are used to instantiate the expensive object. The proxy manages the lifetime of the real subject in the implementation. It decides the need for the instance creation and when to reuse it. Virtual proxies optimize performance.

**Caching proxies**
Caching proxies are used to cache expensive calls to the real subject. There are many caching strategies that the proxy can use. Some of them are read-through, write-through, cache-aside, and time-based. The caching proxies are used for enhancing performance.

**Remote proxies**
Remote proxies are used in distributed object communication. The remote proxy causes execution on the remote object by invoking a local object method.

**Smart proxies**
Smart proxies are used to implement log calls and reference counting to the object.

## 25) Explain the advantage of Chain of Responsibilities Pattern and when it is used?
* It minimizes the coupling.
* It provides flexibility while assigning the responsibilities to objects.
* It permits a set of classes to act as one. The events produced in one class can be sent to other handler classes with the help of composition.
Usage of Chain of Responsibility Pattern

**It is used in the following cases:**

* When more than one objects are ready to handle a request, and the handler is unknown.
* In case the collection or a group of objects that can handle the request must be specified dynamically.

## 26) How is Bridge pattern is different from the Adapter pattern?
The motive of the Adapter pattern is to make interfaces of one or more classes to look similar.

The Bridge pattern is designed to isolate a class's interface from its implementation so we can vary or substitute the implementation without changing the client code.

## 27) What's the difference between the Dependency Injection and Service Locator patterns?
The service locator is used to create class dependencies. The Class is still responsible for creating its dependencies no matter whether if it is using service locator or not. Service locators are also used to hide dependencies. We can't say by looking at an object whether it connects with a database or not when it obtains connections from a locator.

With Dependency injection, the class which contains its dependencies neither knows nor cares where they came from. One significant difference is that Dependency injection is much easier to unit test because we can pass in it mock implementations of its dependent objects. We could combine the two objects and apply the service locator.

## 28) What is the decorator pattern in Java explain it with an example?
The decorator pattern is one of the popular Java design patterns. It is common because of its heavy usage in java.io (package). The Decorator Pattern uses composition in place of inheritance to extend the functionality of an object at runtime.

**BufferedReader** and **BufferedWriter** are some excellent examples of decorator pattern in Java.

## 29) Explain Structural Patterns in Java?
Structural patterns are used to provide solutions and efficient standards regarding class compositions and object structures. They depend on the concept of inheritance and interfaces to allow multiple objects or classes to work together and form a single working whole.

Structural design patterns are responsible for how classes and objects can be composed to form larger structures.

## 30) What Is Factory Pattern?
* It is the most used design pattern in Java.
* These design patterns belong to the Creational Pattern as this pattern provides one of the best ways to create an object.
* In the Factory pattern, we don't expose the creation logic to the client and refer the created object using a standard interface.
* Factory Pattern allows the sub-classes to choose the type of objects to create.
* The Factory Pattern is also known as Virtual Constructor.

## 31) What are the Creational Patterns?
Creational design patterns are related to the way of creating objects. Creational design patterns are used when a decision is made at the time of instantiation of a class.

* **EmpRecord e1=new EmpRecord();**

Since new keyword is used to create an object in Java, So, here we are creating the instance using the new keyword. In some cases, the nature of the object must be changed according to the nature of the program. In such cases, we should use the creational design patterns to provide a more general and flexible approach.

## 32) What Is Gang of Four (GOF)?
In 1994, four authors Erich Gamma, Ralph Johnson, Richard Hel, and John Vlissides published a book titled Design Patterns Elements of Reusable Object-Oriented Software. This book introduced the concept of Design Pattern in Software development.

These four authors are known as Gang of Four GOF.

