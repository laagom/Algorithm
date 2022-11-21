def solution(s):
    answer = ''
    
    temp = sorted(list(s))
  
    for char in temp:
        if temp.count(char) == 1:
            answer += char
    
    return answer