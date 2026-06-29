# 문제: 옷가게 할인 받기
# 난이도: Lv.0 / 체감: ⭐⭐
# 핵심: 조건문 순서, else 처리, int() 형변환
# 복습: 2026-06-30, 2026-07-02, 2026-07-06

# 오답
def solution(price):
    if 300000 > price >= 100000:
        return int(price * 0.95)
    elif 500000 > price >= 300000:
        return int(price * 0.9)
    elif 1000000 > price >= 500000:
        return int(price * 0.8)
    
# 고침
def solution(price):
    if price >= 500000:
        return int(price * .80)
    elif price >= 300000:
        return int(price * .90)
    elif price >= 100000:
        return int(price * .95)
    else: 
        return price # 10만원 미만일때의 return 안했음
    # 그리고 int() 강제 형 변환 꼭 해줘야 했음
    # 80/100 보단 0.8으로 계산. (.8도 되긴 하더라. 축약 표현임)