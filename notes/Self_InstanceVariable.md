# self와 Instance Variable

`self`는 **그 메서드가 호출된 객체 자신을 가리키는 참조**다. Python이 메서드를 호출할 때 자동으로 첫 번째 인자로 넘겨준다.

```python
dog.eat()
```

이렇게 쓰면 Python은 내부적으로 다음처럼 실행한다.

```python
Animal.eat(dog)
```

즉 `eat(self)` 안에서 `self`는 `dog` 그 자체다. `self`라는 **이름 자체는 코드 어디서나 고정**이고, **그 이름이 실제로 가리키는 대상(객체)만 호출할 때마다 달라진다.**

```python
car2.drive()   # 이 순간 self = car2
car1.stop()    # 이 순간 self = car1
```

`id()`로 확인하면 `drive()` 안의 `self`가 `car2`와 정확히 같은 메모리 주소를 가진다.

## self는 입력값이 아니다

`Car("Toyota", 2020, "red", True)`처럼 호출할 때, 우리가 직접 입력하는 값은 4개(`model`, `year`, `color`, `for_sale`)뿐이다. `self`는 그중 하나가 아니라, **Car(...)가 호출되는 순간 Python이 새로 만든 빈 객체**가 자동으로 채워 넣는 자리다.

```python
def __init__(self, model, year, color, for_sale):
```

| 매개변수 | 값 | 채우는 주체 |
|---|---|---|
| `self` | 새로 생성 중인 객체 자체 | Python이 자동으로 |
| `model`, `year`, `color`, `for_sale` | 우리가 넣은 값 | 우리가 직접 입력 |

## local variable vs instance variable

`__init__`의 매개변수(`model`, `year` 등)는 **local variable**이다. `__init__` 실행이 끝나면 사라진다.

```python
def __init__(self, model):
    self.model = model   # local variable(model)의 값을 instance variable(self.model)로 복사해서 영구 저장
```

- `model` (local variable) → `__init__` 실행 중에만 존재, 다른 메서드에서 접근 불가
- `self.model` (instance variable) → 객체가 살아있는 동안 계속 존재, 어떤 메서드에서든 `self.model`로 접근 가능

`self.` 없이 `model = model`만 쓰면 객체 안에 아무것도 저장되지 않아서, 나중에 다른 메서드에서 `self.model`을 읽으려 할 때 `AttributeError: 'Car' object has no attribute 'model'`이 난다.

비유: local variable은 문 앞에 물건을 놓고 바로 떠나는 배달원, `self.model = model`은 그 물건을 집(객체) 창고에 옮겨 담는 행위. 창고에 안 옮기면(`self.` 안 쓰면) 배달원이 떠난 뒤 물건도 같이 사라진다.

## 정리

- `self`는 "지금 이 메서드를 호출한 객체 자신"을 뜻하는 자동 전달 참조
- `self`라는 이름은 고정, 가리키는 대상은 호출마다 달라짐
- `self.속성 = 매개변수`는 local variable을 instance variable로 승격시켜, 그 객체가 살아있는 동안 다른 메서드에서도 재사용할 수 있게 만드는 것