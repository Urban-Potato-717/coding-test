#배열 중 최빈값을 return (최빈값이 여러 개면 -1 return)
def solution(array):
    freq={}
    for num in array:
        # freq[num]은 key로 value를 꺼내는 문법
        # freq 라는 딕셔너리에 num 에 해당하는 key가 있는지 찾는다
        if num in freq:
            # num 이라는 key의 value에 "1을 더한다"
            freq[num] += 1
        else:
            # num 이라는 key로, 1 이라는 value의 키:값을 새로 만든다.
            freq[num] = 1
    '''
    1. 딕셔너리의 기본 동작
    array에서 숫자를 하나씩 꺼내 num에 담고 freq 딕셔너리에 넣으면, num이 **key**가 된다.
    if num in freq를 통해, 처음 보는 숫자면 value로 1을 준다. ({1:1}이 처음으로 생성되는 것)
    값이 있으면 +=1로 해당 key의 value를 1씩 높여준다. (count의 역할을 수행)
    '''
    max_count = max(freq.values())
    '''
    2. freq.values() -> key는 필요 없고 **value (여기서는 횟수)**만 볼 때 쓴다.
    max(freq.values())를 사용하면 max()를 통해 주어진 value 중 가장 큰 값을 구한다. 
    '''
    modes=[key for key, value in freq.items() if value == max_count]
    if len(modes) > 1:
        return -1
    else:
        return modes[0]
    '''
    3. freq.items() -> key, value 전부 가져온다.
    if 문을 통하여 value가 max_count인 key, 즉, 가장 많이 있는 수를 파악한다.
    만약 max_count가 1개 이상 **최다 빈출값 동일**시, modes 라는 배열에 2개 이상의 값이 담기니, 이를 기본으로 return 시 -1 혹은 1을 해준다.
    '''
