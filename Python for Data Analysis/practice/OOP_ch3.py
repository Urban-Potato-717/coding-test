# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code resuability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal): # Dog inherit Animal
    pass           # class Dog only have "pass". But It can use Animal's __init__, eat(), sleep().

class Cat(Animal):
    def speak(self):
        print("MEOW!") # You can add special methods for each class

class Mouse(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
cat.sleep()
mouse.sleep()
cat.speak()