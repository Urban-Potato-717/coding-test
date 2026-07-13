"""OOP Chapter 2: 클래스 변수와 인스턴스 변수.

학습 목표:
- 인스턴스 변수는 객체마다 별도로 저장된다.
- 클래스 변수는 같은 클래스로 만든 모든 객체가 공유한다.
- 클래스 변수는 클래스 이름으로 접근하면 의도가 분명하다.

복습 질문:
- Student.num_students를 self.num_students로 증가시키지 않은 이유는 무엇인가?
- student1.name과 Student.class_year의 소유 범위는 어떻게 다른가?
"""


class Student:
    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(student1.name)
print(student2.age)
print(Student.class_year)
print(Student.num_students)
print(
    f"My graduating class of {Student.class_year} "
    f"has {Student.num_students} students"
)

for student in [student1, student2, student3, student4]:
    print(student.name)
