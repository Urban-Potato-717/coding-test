# 리스트와 딕셔너리

## 한 줄 설명

- 리스트는 값의 순서를 기준으로 저장하고 정수 인덱스로 접근한다.
- 딕셔너리는 직접 정한 key와 value의 관계로 값을 저장한다.

## 언제 떠올리는가

- 순서대로 값을 모으거나 위치가 중요하면 리스트
- 이름이나 숫자 등의 key로 값을 찾거나 등장 횟수를 세면 딕셔너리

## 내가 헷갈린 부분

빈도표에서는 숫자 자체를 key로, 등장 횟수를 value로 저장한다.

```python
frequencies = {1: 2, 3: 1}
# 숫자 1은 두 번, 숫자 3은 한 번 등장
```

## 최소 예제

```python
numbers = [10, 20, 30, 40]
print(numbers[2])  # 30

frequencies = {}
for number in [1, 1, 3]:
    if number in frequencies:
        frequencies[number] += 1
    else:
        frequencies[number] = 1
```

## 딕셔너리에서 꺼내기

```python
frequencies.keys()    # key만
frequencies.values()  # value만
frequencies.items()   # key와 value를 함께
```

## 관련 문제

- `programmers/0623_mode.py`: 숫자별 등장 횟수와 최빈값 계산

## 복습 질문

1. 최빈값을 구할 때 딕셔너리가 자연스러운 이유는 무엇인가?
2. 횟수만 필요할 때 어떤 메서드를 사용하는가?
3. key와 value를 함께 순회하는 코드를 작성할 수 있는가?
