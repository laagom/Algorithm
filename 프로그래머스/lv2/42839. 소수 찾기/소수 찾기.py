# 3번. 소수 찾기

from itertools import permutations

def solution(numbers):
    answer = 0
    li_P = []
    for i in range(1,len(numbers)+1):
        li_P.extend([int(''.join(p)) for p in permutations(numbers, i)])

    li_P = set(li_P)

    for prime in li_P:
        if prime >= 2:
            check = True
            for j in range(2,int(prime**0.5) + 1): 
                if prime % j == 0: 
                    check = False
                    break
            if check:
                answer += 1
    return answer
        
# solution("011")