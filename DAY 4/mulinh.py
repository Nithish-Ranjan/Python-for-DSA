class father:
    def __init__(self, father_name):
        self.father_name = father_name
        
class mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name
        
class child(father, mother):
    def __init__(self, name, father_name, mother_name):
        father.__init__(self, father_name)
        mother.__init__(self, mother_name)
        self.name = name
        
    def display(self):
        print(f"Child Name: {self.name}, Father Name: {self.father_name}, Mother Name: {self.mother_name}")
        
s = child("ABC", "DEF", "GHI")
s.display()