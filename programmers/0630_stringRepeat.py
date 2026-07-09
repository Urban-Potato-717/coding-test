# 문제: 문자 반복 출력하기
# 난이도: Lv.0 / 체감: ⭐⭐
# 핵심: 문자열 직접 순회, 문자열 곱셈, 누적 문자열 만들기

# 나의 풀이
def solution(my_string, n):
    answer = ''
    for string in my_string:
        answer += string * n # 문자열을 이어 붙여 새 문자열 만듦.
    return answer
