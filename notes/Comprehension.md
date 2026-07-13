# 리스트 컴프리헨션

## 한 줄 설명

반복하면서 값을 변환하거나 조건에 맞는 값만 골라 새로운 리스트를 만드는 문법이다.

## 언제 떠올리는가

- 반복문의 결과를 새로운 리스트에 담을 때
- 기존 리스트의 모든 값을 같은 규칙으로 변환할 때
- 조건을 만족하는 값만 골라낼 때

## 내가 헷갈린 부분

컴프리헨션 맨 앞의 표현식이 최종 리스트에 저장되는 값이라는 점이 헷갈렸다.

```python
modes = [
    key
    for key, value in frequencies.items()
    if value == max_count
]
```

구조는 `[저장할 값 | 반복하며 꺼낼 값 | 포함 조건]`이다. 위 코드에는 조건을 만족하는 `key`만 저장된다.

## 최소 예제

```python
evens = []
for number in range(10):
    if number % 2 == 0:
        evens.append(number)

evens = [number for number in range(10) if number % 2 == 0]
doubled = [number * 2 for number in [1, 2, 3]]
```

## 언제 사용하지 않는가

조건과 변환이 복잡해서 한 번에 읽기 어렵다면 일반 반복문이 더 낫다.

## 관련 문제

- `programmers/0623_mode.py`: 가장 많이 등장한 횟수를 가진 key 선택

## 복습 질문

1. `[number * 2 for number in numbers]`에서 최종 저장되는 값은 무엇인가?
2. 짝수만 고르는 코드를 반복문과 컴프리헨션으로 각각 작성할 수 있는가?
3. `(key, value)`를 모두 저장하려면 어느 부분을 바꿔야 하는가?
