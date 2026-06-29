# 문제: 피자 나눠먹기 (3)
# 난이도: Lv.0 / 체감: ⭐⭐
# 핵심: 올림 나눗셈, (n-1)//slice + 1 패턴
# 복습: 2026-06-30, 2026-07-02, 2026-07-06

def solution(slice, n):
    if n % slice == 0:
        return n // slice
    else:
        return n // slice + 1

# 다른 사람의 풀이
def solution(slice, n):
    #올림 나눗셈
    return ((n - 1) // slice) + 1
