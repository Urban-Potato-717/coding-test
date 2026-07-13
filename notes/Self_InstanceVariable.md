# self와 인스턴스 변수

## 한 줄 설명

`self`는 현재 메서드를 호출한 객체 자신이고, `self.attribute`는 그 객체가 살아 있는 동안 보관하는 값이다.

## 언제 떠올리는가

- 클래스의 여러 메서드가 같은 값을 사용해야 할 때
- 객체마다 서로 다른 상태를 저장해야 할 때
- `AttributeError`가 발생해 객체에 속성이 저장됐는지 확인할 때

## 내가 헷갈린 부분

`self`를 객체를 만들 때 직접 전달하는 입력값으로 생각했다. 실제로는 Python이 새 객체를 만들고 메서드의 첫 번째 인자로 자동 전달한다.

```python
dog.eat()
Animal.eat(dog)  # 내부적으로 이와 비슷하게 호출
```

## 최소 예제

```python
class Car:
    def __init__(self, model):
        self.model = model

    def describe(self):
        return self.model


car = Car("Mustang")
print(car.describe())  # Mustang
```

## 지역 변수와 인스턴스 변수

- `model`: `__init__`이 실행되는 동안만 사용하는 지역 변수
- `self.model`: 객체에 저장되어 다른 메서드에서도 사용하는 인스턴스 변수

`model = model`만 작성하면 객체에 값이 저장되지 않는다.

## 관련 실습

- `Python OOP/practice/car.py`: 인스턴스 변수와 메서드
- `Python OOP/practice/OOP_ch1.py`: 두 객체의 서로 다른 상태 확인

## 복습 질문

1. `car.drive()`를 클래스 이름을 사용한 호출 형태로 바꿔 쓸 수 있는가?
2. `model`과 `self.model`의 수명은 어떻게 다른가?
3. `self.`를 생략하면 다른 메서드에서 값을 사용할 수 없는 이유는 무엇인가?
