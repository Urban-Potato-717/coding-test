"""문자 반복 출력하기.

결과: 해결
체감 난이도: 2/5
핵심: 문자열 직접 순회, 문자열 곱셈, 문자열 누적

학습 기록:
- 문자열을 직접 순회하면 문자를 하나씩 꺼낼 수 있다.
- character * n으로 같은 문자를 n번 반복한다.
"""


def solution(my_string, n):
    answer = ""

    for character in my_string:
        answer += character * n

    return answer
