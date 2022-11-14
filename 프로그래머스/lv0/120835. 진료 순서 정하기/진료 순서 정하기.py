def solution(emergency):
    answer = []
    
    list = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(list.index(i)+1)
        
    return answer