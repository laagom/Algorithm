def solution(n):
    answer = "수박"*(int((n+1)/2))
    return answer if n%2 == 0 else answer[:-1]