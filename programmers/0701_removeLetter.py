def solution(my_string, letter):
    answer=""
    for char in my_string:
        if char != letter:
            answer += char
    return answer

# 문자열에는 remove()가 없다
# range에는 integer만 넣을 수 있다. my_string은 문자열이라서, 문자열 "직접 순회"가 필요하다.