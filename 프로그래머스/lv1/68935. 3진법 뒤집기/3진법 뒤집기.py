def solution(n):
    answer = ""
    
    # 다시 한버 풀어보기
    while n>0:
        n, re = divmod(n,3)
        answer += str(re)
        
    return int(answer, 3)

