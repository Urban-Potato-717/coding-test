"""OOP Chapter 1: 클래스와 객체.

학습 목표:
- 클래스는 객체의 구조를 정의하는 설계도라는 점을 확인한다.
- 같은 Car 클래스로 서로 다른 상태를 가진 객체를 만든다.
- 인스턴스 변수와 메서드에 접근한다.

복습 질문:
- car2.drive()를 호출할 때 drive()의 self는 어떤 객체인가?
- car1과 car2의 model 값이 서로 다른 이유는 무엇인가?

관련 노트:
- notes/Self_InstanceVariable.md
"""

from car import Car


car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)

print(car2)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car2.drive()
car1.stop()
car1.describe()
