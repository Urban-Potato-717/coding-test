# 문제: 짝수 홀수 개수
# 난이도: Lv.0 / 체감: ⭐⭐
# 핵심: 나머지 연산 %, 카운터 변수, 결과 리스트 인덱스

# 나의 풀이
def solution(num_list):
    even = 0
    odd = 0
    for x in num_list:
        if x % 2 == 0:
            even += 1
        else: 
            odd +=1
    return [even,odd]

# 다른 사람의 풀이 1 - 각 숫자를 순회하며 위치를 1씩 증가시킴
def solution(num_list):
    answer = [0,0]
    for x in num_list:
        if x % 2 == 0:
            answer[0] += 1
        else: 
            answer[1] +=1
    return answer
