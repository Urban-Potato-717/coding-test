# 나의 풀이
def solution(my_string, n):
    answer = ''
    for string in my_string:
        answer += string * n # 문자열을 이어 붙여 새 문자열 만듦.
    return answer