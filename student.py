# Define a Student class
class Student:
    def _init_(self, name, roll_no, course, marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def display(self):
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print(f"Course   : {self.course}")
        print(f"Marks    : {self.marks}")

# Sample student data
student_list = [
    Student("Akshata Patil", "101", "Computer Science", 88.5),
    Student("Sneha Rao", "102", "Electronics", 92.0),
    Student("Rahul Desai", "103", "Mechanical", 76.5),
    Student("Priya Kulkarni", "104", "Civil", 81.0),
    Student("Anil Joshi", "105", "Information Science", 89.0)
]

# Display all students
print("\n--- Sample Student Details ---")
for i, student in enumerate(student_list, start=1):
    print(f"\nStudent {i}:")
    student.display()