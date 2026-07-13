"""배열 뒤집기.

결과: 오답 수정
체감 난이도: 2/5
핵심: 슬라이싱, 뒤집기와 정렬의 차이

오답 원인:
- sort(reverse=True)를 사용했지만 이것은 현재 순서를 뒤집지 않고 값을 내림차순으로 정렬한다.

해결:
- [::-1]로 현재 배열의 역순인 새 리스트를 만든다.
- reverse()도 가능하지만 원본을 변경하고 반환값은 None이다.

관련 노트:
- notes/Slicing.md
"""


def solution(num_list):
    return num_list[::-1]
