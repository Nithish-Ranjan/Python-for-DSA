class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class student(person):
    def __init__(self, name, age, roll_number, marks):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.marks = marks
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll Number: {self.roll_number}, Marks: {self.marks}")
        
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter the name of the student: ")
    age = int(input("Enter the age of the student: "))
    roll_number = int(input("Enter the roll number of the student: "))
    marks = float(input("Enter the marks of the student: "))
    
    s = student(name, age, roll_number, marks)
    s.display()