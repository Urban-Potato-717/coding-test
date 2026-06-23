#배열을 정렬하고 중앙값 return하기
def solution(array):
    array.sort()
    return array[len(array)//2]

'''
1. 배열의 정렬
.sort() - 기본 ASC / .sort(reverse=True) - DESC
중앙 값을 구하는 것은 어떤 정렬도 상관없으니 문제에서는 .sort() 사용

**sort()는 원본을 변경하지만, sorted()는 변경하지 않음!**

2. // 몫 나누기를 사용해 절반으로 나누면, 중앙 인덱스가 나옴
짝수 개일 때는 중앙값이 없음.
'''