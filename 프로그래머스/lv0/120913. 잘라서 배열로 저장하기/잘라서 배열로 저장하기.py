from collections import deque

def solution(my_str, n):
    answer = []
    string  = ''
    
    de = deque(my_str)
    
    for char in deque(my_str):
        string += de.popleft()
        
        if len(string) == n or len(de) == 0:
            answer.append(string)
            string = ''
    
    return answer