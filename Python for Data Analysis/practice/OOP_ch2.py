# class Variables = Shared among all instances of a class
#                   Defined *outside* the constructur
#                   Allow you to share data among objects created from that class

class Student:
    # class variables
    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        # instance variables (self, each object have their own)
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(student1.name)
print(student2.age)
print(Student.class_year) # access class variables by class name itself

print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)