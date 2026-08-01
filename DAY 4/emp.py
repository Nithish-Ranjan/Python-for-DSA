class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class developer(employee):
    def __init__(self, name, salary, prog_lang):
        super().__init__(name, salary)
        self.prog_lang = prog_lang

class hr(developer):
    def __init__(self, name, salary, prog_lang, department):
        super().__init__(name, salary, prog_lang)
        self.department = department

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Programming Language: {self.prog_lang}, Department: {self.department}")
        
c = hr("YASH", 600000, "Python", "Human Resources")
c.display()