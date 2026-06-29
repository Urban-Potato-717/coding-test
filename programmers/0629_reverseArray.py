# 문제: 배열 뒤집기
# 난이도: Lv.0 / 체감: ⭐⭐⭐
# 핵심: 슬라이싱 [::-1], reverse() vs sort(reverse=True) 차이
# 복습: 2026-06-30, 2026-07-02, 2026-07-06

def solution(num_list):
    num_list.sort(reverse=True)
    answer = [x for x in num_list]
    return answer

'''
테스트 3에서 오류가 남. 왜? -> sort(reverse=True)는 "내림차순"이지 뒤집기가 아님. 그래서 위는 틀림 그냥
'''
#다른 사람의 풀이
def solution(num_list):
    return num_list[::-1] #뭐여 이거 어캐푼거임 쌰갈
'''
슬라이싱 기본 문법
list[시작:끝:간격] < 모두 생략 가능하고, 생략 시 기본값을 준다.
해당 문제와 같은 경우는 step에 -1로 전체 뒤집기를 진행함. 음수 step = 뒤집기
'''
#생각해보니 더 좋을거같은 가독성
def solution(num_list):
    num_list.reverse() #반환하는게없음. return에는 다른 값을 줘야함
    return num_list
