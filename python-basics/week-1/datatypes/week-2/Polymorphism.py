# Week 2 - Day 5 (Polymorphism)

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

class Cow:
    def sound(self):
        print("Cow moos")


# Same method name, different behavior
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
