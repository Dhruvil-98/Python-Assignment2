# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XEgz_1YkeaNU4GKL-7aY86nyKqxyoTMT
"""

#Question 1
class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

    def display_info(self):
        print(f"Vehicle Name: {self.name_of_vehicle}")
        print(f"Maximum Speed: {self.max_speed} mph")
        print(f"Average Fuel Consumption: {self.average_of_vehicle} mpg")


my_car = Vehicle("Toyota Camry", 120, 30)

my_car.display_info()

#Question 2
class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display_info(self):
        return f"Name: {self.name}, Color: {self.color}"

class Car(Vehicle):
    def __init__(self, name, color, brand):
        super().__init__(name, color)
        self.brand = brand

    def seating_capacity(self, capacity):
        return f"{self.name} by {self.brand} has a seating capacity of {capacity} people"


my_car = Car("Sedan", "Blue", "ABC Motors")
capacity = 5
print(my_car.display_info())
print(my_car.seating_capacity(capacity))

#Question 4
class Person:
    def __init__(self, name, age, gender):
        self.__name = name  # Encapsulation: Make age property private
        self.__age = age
        self.gender = gender

    def say_hello(self):
        print(f"Hello, my name is {self.__name}.")

    def is_adult(self):
        return self.__age >= 18

    # Encapsulation: Create a method to allow access to the private age property
    def get_age(self):
        return self.__age

class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course

    def get_student_info(self):
        return f"Student ID: {self.student_id}, Name: {self._Person__name}, Age: {self.get_age()}, Gender: {self.gender}, Course: {self.course}"

class Teacher(Person):
    def __init__(self, name, age, gender, teacher_id, subject):
        super().__init__(name, age, gender)
        self.teacher_id = teacher_id
        self.subject = subject

    def say_hello(self):  # Polymorphism: Override say_hello() for Teacher
        print(f"Hello, I am {self._Person__name}, your {self.subject} teacher.")

# Example usage:
person1 = Person("Alice", 25, "Female")
person1.say_hello()
print(f"Is {person1._Person__name} an adult? {person1.is_adult()}")

student1 = Student("Bob", 19, "Male", "12345", "Computer Science")
student1.say_hello()
print(student1.get_student_info())
print(f"Is {student1._Person__name} an adult? {student1.is_adult()}")

teacher1 = Teacher("Mr. Smith", 35, "Male", "T123", "Math")
teacher1.say_hello()
print(f"Is {teacher1._Person__name} an adult? {teacher1.is_adult()}")

