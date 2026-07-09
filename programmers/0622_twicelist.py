# 문제: 배열 두배 만들기
# 난이도: Lv.0 / 체감: ⭐⭐
# 핵심: 반복문, 리스트 append
def solution(numbers):
    answer=[]
    for idx in range(len(numbers)):
        a = numbers[idx] * 2
        answer.append(a)
    return answer 


"""
1. 파이썬의 반복문은 "for 변수 in 반복 횟수:"로 사용한다.
ex) for a in range(5) # 0,1,2,3,4 순서로 5번 **순회**한다.

2. 리스트 길이는 len(리스트 이름)이다.
len은 **길이를 셀 수 있는 것**에 모두 사용한다.
"""
