def solution(n, t):
    answer = n
    
    for _ in range(1, t+1):
        answer *= 2
    print(answer)
    return answer