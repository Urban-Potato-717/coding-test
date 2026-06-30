# blueprint of class Car
class Car:
    # __init__ is "constructor" 
    def __init__(self, model, year, color, for_sale):
        self.model = model      # model attributes of object itself.
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    # methods - actions that object can do
    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")
    
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")