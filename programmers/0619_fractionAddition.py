#분수의 덧셈
def solution(numer1, denom1, numer2, denom2):
    #공통 분수 만들어 더하기
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    #!유클리드 호제법 구현 함수 - 나머지가 0이 될 때까지 반복(a,b)->(b,a%b)
    def gcd(a,b):
        while b != 0:
            #* 파이썬 변수 교체 원리  - 오른쪽 전체 먼저 계산 후 한번에 대입
            a, b = b, a % b
        return a
    
    g = gcd(numer, denom)
    return [numer//g, denom//g]