"""배열 원소의 평균값.

결과: 해결
체감 난이도: 1/5
핵심: sum(), len()

학습 기록:
- 반복문으로 합계를 누적할 수 있지만 sum(numbers)가 의도를 더 직접적으로 표현한다.
"""


def solution(numbers):
    return sum(numbers) / len(numbers)
