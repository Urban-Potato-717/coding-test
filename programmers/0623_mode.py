#배열 중 최빈값을 return (최빈값이 여러 개면 -1 return)
def solution(array):
    freq={}
    for num in array:
        if num in freq:
            freq[num] += 1
        else:
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
    3. modes 
    이걸 풀어쓰면:
    modes = []
    for k, v in freq.items():
      if v == max_count:
          modes.append(k)

    여기서 freq.items()를 알아야 하는데, 이는 key, value를 쌍으로 꺼낸다.
    그래서 k에 key를, v에 value를 담는거임.
    '''
    return