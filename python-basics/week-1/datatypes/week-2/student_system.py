# Week 2 - Day 7 (Mini Project)

students = []

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    
    student = {
        "name": name,
        "age": age
    }
    
    students.append(student)
    print("Student added!\n")


def show_students():
    if len(students) == 0:
        print("No students found\n")
    else:
        for i, s in enumerate(students, start=1):
            print(f"{i}. Name: {s['name']} | Age: {s['age']}")
        print()


while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        print("Goodbye ")
        break
    else:
        print("Invalid choice\n")
