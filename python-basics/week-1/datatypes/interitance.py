# Week 2 - Day 3 (Inheritance)

# Parent class
class Person:
    
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


# Child class
class Student(Person):
    
    def __init__(self, name, marks):
        super().__init__(name)   # parent ka constructor call
        self.marks = marks

    def show_marks(self):
        print("Marks:", self.marks)


# Object
s1 = Student("Ali", 88)

s1.show_name()   # parent method
s1.show_marks()  # child method
