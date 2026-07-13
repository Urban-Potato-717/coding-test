"""직각 이등변 삼각형 출력하기.

결과: 해결
체감 난이도: 2/5
핵심: input() 형변환, range(), 문자열 반복

학습 기록:
- range의 stop 값은 포함되지 않으므로 1부터 n까지는 range(1, n + 1)이다.
- "*" * length로 별을 행 길이만큼 반복한다.
"""


height = int(input())

for length in range(1, height + 1):
    print("*" * length)
