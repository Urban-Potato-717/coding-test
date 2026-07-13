"""피자 나눠 먹기 (3).

결과: 해결, 한 줄 공식 비교
체감 난이도: 2/5
핵심: 올림 나눗셈

학습 기록:
- 나누어떨어지면 몫만, 나머지가 있으면 한 판을 더한다.
- 양의 정수 n에서는 (n - 1) // slice + 1로 같은 계산을 표현할 수 있다.

관련 노트:
- notes/CeilingDevision.md
"""


def solution(slice, n):
    return (n - 1) // slice + 1
