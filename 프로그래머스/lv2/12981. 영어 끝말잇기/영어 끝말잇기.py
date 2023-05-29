import copy
import collections
def solution(n, words):
    metion = []
    before = ""
    arr = collections.deque(copy.copy(words))  
    for i, word in enumerate(words):
        # 끝자리의 스펠링으로 시작하지 않는 경우
        if i > 0 and word[0] != before[-1]:
            return [i%n+1, i//n+1] 
        
        # 이전에 언급한 단어가 반복
        if word in metion:
            return [i%n+1, i//n+1]
        
        # 이전에 언급한 단어 모음
        before  = word
        metion.append(arr.popleft())

    return [0, 0]