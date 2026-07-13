"""OOP Chapter 4: 다단계 상속과 다중 상속.

학습 목표:
- 다단계 상속은 부모가 물려받은 기능을 자식도 사용하는 구조다.
- 다중 상속은 하나의 클래스가 둘 이상의 부모 기능을 물려받는 구조다.

직접 확인:
- Rabbit은 Prey를 거쳐 Animal.eat()을 사용한다.
- Fish는 Prey.flee()와 Predator.hunt()를 모두 사용한다.

복습 질문:
- Fish가 eat(), flee(), hunt()를 모두 사용할 수 있는 경로를 설명할 수 있는가?
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
hawk.hunt()
fish.flee()
fish.hunt()
