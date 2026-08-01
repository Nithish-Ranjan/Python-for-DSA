class car:  
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
        
s = car("Toyota", "Camry", 2020)
s.display()