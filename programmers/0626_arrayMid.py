# 배열 원소의 평균값 구하기
def solution(numbers):
    num = 0
    for x in numbers:
        num += x
    return num / len(numbers)

# 다른 사람의 풀이
def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer
# sum(리스트) - 리스트 전체를 다 더해주는 내장 함수.