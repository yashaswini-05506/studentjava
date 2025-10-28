class Student:
    def __init__(self, name, roll_no, course, marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def display(self):
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print(f"Course   : {self.course}")
        print(f"Marks    : {self.marks}")
        print("-" * 30)

# Sample student objects
students = [
    Student("Akshata Patil", "101", "Computer Science", 88.5),
    Student("Ravi Kumar", "102", "Mechanical Engineering", 76.0),
    Student("Sneha Reddy", "103", "Electronics", 91.2)
]

# Display all student details
for student in students:
    student.display()