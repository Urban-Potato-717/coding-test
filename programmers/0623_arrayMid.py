"""중앙값 구하기.

결과: 해결
체감 난이도: 2/5
핵심: 정렬, 중앙 인덱스, 정수 나눗셈

학습 기록:
- 중앙값을 찾기 전에 배열을 정렬해야 한다.
- sorted()는 새 리스트를 만들고, list.sort()는 원본을 변경한다.
"""


def solution(array):
    sorted_array = sorted(array)
    middle_index = len(sorted_array) // 2
    return sorted_array[middle_index]
