# Python-Assignment2
Question - 1
Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed and average_of_vehicle.

Question - 2
Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class. Create a method named seating_capacity which takes capacity as an argument and returns the name of the vehicle and its seating capacity.

Question - 3 
What is multiple inheritance? Write a python code to demonstrate multiple inheritance.
Multiple inheritance is a feature in some object-oriented programming languages that allows a class to inherit properties and behaviors from more than one parent class or superclass. 
In multiple inheritance, a subclass can inherit attributes and methods from multiple parent classes. This is in contrast to single inheritance, where a class can inherit from only one parent class.

Question - 4
Objective: To create Python classes implementing the concepts of polymorphism, encapsulation, constructors, and inheritance.

Task 1: Create a Python Class
Create a class called Person with the following:
1. Properties: name, age, gender
2. A constructor to initialize these properties.
3. Methods: say_hello(), which prints out a greeting from the person; and is_adult(), which returns True if the person is 18 or above, and False otherwise.
   
Task 2: Implement Inheritance
Create a subclass called Student that inherits from the Person class. The Student class should have the following additional properties:
1. student_id
2. course
Create appropriate methods as you deem necessary.

Task 3: Implement Polymorphism
Create another subclass called Teacher that also inherits from the Person class. The Teacher class should have the following additional properties:
1. teacher_id
2. subject
Ensure that the say hello() method for the Teacher class is different from the one for
the Person and Student classes. This will demonstrate polymorphism.

Task 4: Encapsulation
Make the age property in the Person class private and create a method to allow access to it. This is an example of encapsulation, as it restricts direct access to the age property.
