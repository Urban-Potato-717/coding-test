"""분수의 덧셈.

결과: 해결
체감 난이도: 5/5
핵심: 분수 통분, 유클리드 호제법, 최대공약수

막힌 부분:
- 더한 분수를 가장 간단한 형태로 약분하는 과정이 어려웠다.

다음에 떠올릴 신호:
- 분수를 기약분수로 만들라는 조건이 있으면 분자와 분모의 GCD를 구한다.

관련 노트:
- notes/GCD_LCM.md
"""


def solution(numer1, denom1, numer2, denom2):
    numerator = numer1 * denom2 + numer2 * denom1
    denominator = denom1 * denom2

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    common_divisor = gcd(numerator, denominator)
    return [
        numerator // common_divisor,
        denominator // common_divisor,
    ]
