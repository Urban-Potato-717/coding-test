"""짝수 홀수 개수.

결과: 해결
체감 난이도: 2/5
핵심: 나머지, 카운터 변수

학습 기록:
- number % 2가 0이면 짝수이고, 그렇지 않으면 홀수다.
- 반환 순서가 [짝수 개수, 홀수 개수]임을 확인한다.
"""


def solution(num_list):
    even_count = 0
    odd_count = 0

    for number in num_list:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return [even_count, odd_count]
