"""특정 문자 제거하기.

결과: 해결
체감 난이도: 2/5
핵심: 문자열 직접 순회, 조건 필터, 문자열 누적

학습 기록:
- 문자열에는 list.remove()와 같은 remove() 메서드가 없다.
- 문자열을 직접 순회하며 제거할 문자와 다른 문자만 결과에 붙인다.
"""


def solution(my_string, letter):
    answer = ""

    for character in my_string:
        if character != letter:
            answer += character

    return answer
