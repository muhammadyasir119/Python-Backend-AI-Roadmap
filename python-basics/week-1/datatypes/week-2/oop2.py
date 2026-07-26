# Week 2 - Day 2

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def update_marks(self, new_marks):
        self.marks = new_marks
        print("Marks updated!")

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 70:
            return "B"
        else:
            return "C"


# Object
s1 = Student("Ali", 65)

s1.show()

# Update marks
s1.update_marks(85)

s1.show()

# Grade check
print("Grade:", s1.grade())
