def solution(numlist, n):
    
    answer=sorted([i for i in numlist],key=lambda x:(abs(x-n),-x))
    
    
    print(sorted([i for i in numlist],key=lambda x:(abs(x-n),x)))
    
    
    
    
    
    return answer