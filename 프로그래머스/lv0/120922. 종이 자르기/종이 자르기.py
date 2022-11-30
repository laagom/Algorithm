def solution(M, N):
    answer = 0
    # 2 x 2 => 3, 2 x 5 => 9, 4 x 4 => 
    
    
    answer += min(M, N) -1
    
    answer += (max(M, N)-1)*min(M, N)
    
    
    return answer