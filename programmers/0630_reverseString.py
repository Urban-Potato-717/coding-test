"""문자열 뒤집기.

결과: 해결
체감 난이도: 2/5
핵심: 문자열 슬라이싱

학습 기록:
- 문자열도 인덱스로 접근할 수 있는 시퀀스라서 [::-1]을 사용할 수 있다.

관련 노트:
- notes/Slicing.md
"""


def solution(my_string):
    return my_string[::-1]
