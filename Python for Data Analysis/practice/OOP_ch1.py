# Python Object Oriented Programming (OOP)

#* object = A "bundle" of related attributes (variables) and methods (functions)
#           Ex. phone, cup, book
#           You need a "class" to create many objects

#* class = (blueprint) used to design the structure and layout of an object

from car import Car

# making objects with class
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)

print(car2) # memory location (object itself)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car2.drive()
car1.stop()
car1.describe()