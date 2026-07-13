"""배열 두 배 만들기.

결과: 해결
체감 난이도: 2/5
핵심: 리스트 직접 순회, append

학습 기록:
- 인덱스가 필요하지 않다면 range(len(numbers))보다 값을 직접 순회하는 편이 읽기 쉽다.
"""


def solution(numbers):
    answer = []

    for number in numbers:
        answer.append(number * 2)

    return answer
