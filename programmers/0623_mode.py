"""최빈값 구하기.

결과: 해결
체감 난이도: 5/5
핵심: 딕셔너리 빈도표, items(), values(), 리스트 컴프리헨션

막힌 부분:
- 숫자별 횟수를 저장하는 방법과 최대 횟수에 해당하는 key를 찾는 방법이 어려웠다.

원인과 해결:
- 숫자를 key, 등장 횟수를 value로 저장하는 빈도표를 만든다.
- 가장 큰 value를 구한 뒤 해당 value를 가진 key만 선택한다.
- 그런 key가 여러 개면 최빈값이 여러 개이므로 -1을 반환한다.

다음에 떠올릴 신호:
- 값마다 등장 횟수를 세어야 하면 딕셔너리 빈도표를 생각한다.

관련 노트:
- notes/ListVSDictuinary.md
- notes/Comprehension.md
"""


def solution(array):
    frequencies = {}

    for number in array:
        if number in frequencies:
            frequencies[number] += 1
        else:
            frequencies[number] = 1

    max_count = max(frequencies.values())
    modes = [
        key
        for key, value in frequencies.items()
        if value == max_count
    ]

    if len(modes) > 1:
        return -1

    return modes[0]
