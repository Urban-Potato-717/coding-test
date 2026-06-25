# Comprehension

패턴이 있는 list, dictionary, set을 보다 간단하게 작성할 수 있도록 지원한다.

```python
numbers=[]
for n in range(10):
    numbers.append(n)
```
이 코드를 다음과 같이 작성할 수 있다

```python - comprehension
[x for x in range(10)]
```
컴프리헨션에서 사용한 x는 for문 내무에서 append 메소드에 인자로 넣은 변수 n과 같다.

+ if 키워드를 사용할 수 있는데, 이는 for문 다음에 위치해야 한다.
```python
[x for x in range(10) if x % 2 == 0]
```
해당 리스트 컴프리헨션은 **짝수**를 담는다

# 0623_mode 문제를 풀어보자
해당 코드에는 다음과 같은 문법이 나온다
mode = [key for key, value in freq.items() if value == max_count]

구조로 나누어 보면 다음과 같다

  [  key  |  for key, value in freq.items()  |  if value == max_count  ]
   ^^^^^^         ^^^^^^^^^^^^^^^^^^^^^^^          ^^^^^^^^^^^^^^^^^^^^
   결과로          순회하면서 key, value에           조건 필터
   남길 것         값을 담기

즉, **key**만 최종적으로 남긴다. 앞에 부분을 (key, value)로 작성하면, 두 값을 받을 수 있다.
