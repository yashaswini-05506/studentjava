class Student:
    def __init__(self, name, roll_no, age, course):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.course = course

    def display_details(self):
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print(f"Age      : {self.age}")
        print(f"Course   : {self.course}")
        print("-" * 30)

# List of student objects with sample data
students = [
    Student("Yashaswi", "23CS101", 20, "Computer Science"),
    Student("Aarav", "23ME102", 21, "Mechanical Engineering"),
    Student("Ishita", "23EC103", 19, "Electronics & Communication"),
    Student("Rohan", "23EE104", 22, "Electrical Engineering")
]

# Display all student details
print("📋 Student Records\n" + "=" * 30)
for student in students:
    student.display_details()