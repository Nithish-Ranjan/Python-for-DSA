class vehicle:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year
        
class car(vehicle):
    def __init__(self, name, color, year, model):
        super().__init__(name, color, year)
        self.model = model
        
    def display(self):
        print(f"Name: {self.name}, Color: {self.color}, Year: {self.year}, Model: {self.model}")
        
s = car("Toyota", "Red", 2020, "Supra")
s.display()
        