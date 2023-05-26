def solution(arr):
    answer = []
    la = len(arr)
    
    if la == 1:
        return arr
    
    cnt = 0
    while la / 2 != 1:
        if la % 2 == 0:
            la /= 2
        else:
            cnt += 1
            la = len(arr) + cnt
    answer = arr + [0] * cnt
    return answer