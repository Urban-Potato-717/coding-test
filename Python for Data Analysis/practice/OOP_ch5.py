# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
#                 They can contain anbstract methods, which are declared but have no implemenation.
#                 Abstract classes benefits:
#                 1. Prevents instantiation of the class itself
#                 2. Requires children to use inherited abstract methods

# "추상" 클래스: 그 자체로는 객체를 만들 수 없는 (instantiated 할 수 없는) 클래스.
#               Prey(Animal)처럼, 다른 클래스가 상속받아 쓰라고 만든 "설계도용" 클래스. 

# abc means "abstract base classes"
# ABC: 상속받으면 "이 클래스는 추상 클래스다"라고 표시해주는 특수 부모 클래스.
#      추상 메서드가 구현 안 된 채로 남아있는지 실제로 검사(강제)하는 역할.
# abstractmethod: 메서드에 붙이는 데코레이터. "이 메서드는 자식이 반드시 구현해야 함"이라는 표시(라벨)일 뿐,
#                 강제하는 힘은 없음 -> 그래서 ABC와 항상 세트로 사용.
#                 (ABC 없이 abstractmethod만 쓰면 구현 안 해도 그냥 객체 생성됨)
from abc import ABC, abstractmethod

# Parent
# Vehicle(ABC) -> Vehicle 자체는 인스턴스화 불가, 자식이 go/stop을 전부 구현해야만 자식은 인스턴스화 가능
class Vehicle(ABC):

    # 오버라이딩 = 부모 메서드를 자식이 다시 정의하는 것 (상위 개념)
    # 구현 = 몸체가 비어있던 메서드에 처음 동작을 채우는 것
    # 여기 go/stop은 부모(Vehicle)가 pass뿐이라 비어있었으므로,
    # 자식이 다시 쓰는 순간 "오버라이딩"이면서 동시에 "구현"이 됨 (일반 메서드였다면 오버라이딩이어도 구현은 아닐 수 있음)
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Child
class Car(Vehicle):
    
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

# Child
class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

# Child
class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    # TypeError: Can't instantiate abstract class Boat without an implementation for abstract method 'stop'
    # You have to include all methods
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