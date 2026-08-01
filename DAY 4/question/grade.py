class Student:
    def __init__(self, sid, name):
        self.sid = sid          
        self.name = name      



class Subject:
    def __init__(self):
        self.marks = {}        

    def addMarks(self, subject, mark):
        self.marks[subject] = mark

class GradeCalculator:
    def grade(self, avg):
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "Fail"

class ReportCard:

    def __init__(self, student, subject):
        self.student = student
        self.subject = subject
        self.gc = GradeCalculator()

    def display(self):
        total = 0
        print("\n------ REPORT CARD ------")
        print("Student ID :", self.student.sid)
        print("Name       :", self.student.name)
        print("\nSubjects and Marks")

      
        for sub, mark in self.subject.marks.items():
            print(sub, ":", mark)
            total += mark

        avg = total / len(self.subject.marks)

        print("\nTotal   :", total)
        print("Average :", avg)

        print("Grade   :", self.gc.grade(avg))



student = None
subject = Subject()

while True:

    print("\n===== STUDENT GRADE MANAGEMENT =====")
    print("1. Add Student")
    print("2. Add Subject Marks")
    print("3. Display Report Card")
    print("4. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        sid = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        student = Student(sid, name)
        print("Student Added Successfully")

    elif ch == 2:
        sub = input("Enter Subject Name: ")
        mark = int(input("Enter Marks: "))
        subject.addMarks(sub, mark)
        print("Marks Added Successfully")

    elif ch == 3:
        r = ReportCard(student, subject)
        r.display()

    elif ch == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice")