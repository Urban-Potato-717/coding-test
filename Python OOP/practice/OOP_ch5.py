"""OOP Chapter 5: 추상 클래스.

학습 목표:
- 추상 클래스는 직접 객체를 만들기보다 공통 설계를 제공한다.
- 추상 메서드는 자식 클래스가 반드시 구현해야 할 동작을 정의한다.
- ABC와 abstractmethod가 구현 여부를 검사한다.

내가 헷갈린 부분:
- 자식이 추상 메서드를 다시 정의하는 것은 오버라이딩이며, 비어 있던 동작을
  채운다는 의미에서는 구현이기도 하다.

복습 질문:
- Boat에서 stop()을 제거하면 객체를 만들 때 어떤 오류가 발생하는가?
- abstractmethod만 쓰고 ABC를 상속하지 않으면 강제가 되지 않는 이유는 무엇인가?
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")


class Boat(Vehicle):
    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You stop the boat")


car = Car()
car.go()
car.stop()

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()

boat = Boat()
boat.go()
boat.stop()
