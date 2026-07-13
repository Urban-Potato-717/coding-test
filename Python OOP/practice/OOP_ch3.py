"""OOP Chapter 3: 상속.

학습 목표:
- 자식 클래스가 부모 클래스의 속성과 메서드를 재사용한다.
- 자식 클래스에 고유한 메서드를 추가할 수 있다.

복습 질문:
- Dog에 __init__이 없어도 Dog("Scooby")가 가능한 이유는 무엇인가?
- cat.speak()는 가능하지만 dog.speak()는 불가능한 이유는 무엇인가?
"""


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    pass


class Cat(Animal):
    def speak(self):
        print("MEOW!")


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
