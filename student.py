class Student:
    def __init__(self, name, roll_no, age, course):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.course = course

    def display_details(self):
        print("\n--- Student Details ---")
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print(f"Age      : {self.age}")
        print(f"Course   : {self.course}")

# Input from user
name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")
age = int(input("Enter age: "))
course = input("Enter course name: ")

# Create Student object
student1 = Student(name, roll_no, age, course)

# Display student details
student1.display_details()