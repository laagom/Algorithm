from collections import deque
def solution(A, B):
    answer = -1
    
    varchar = deque(A)
    cnt = 0
    
    if A == B:
        return 0
    
    for _ in range(len(B)):
        cnt += 1
        varchar.appendleft(varchar.pop())
        
        if ''.join(varchar) == B:
            return cnt

    return answer