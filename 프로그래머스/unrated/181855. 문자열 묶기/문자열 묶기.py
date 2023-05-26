
def solution(strArr):
    group = {}
    
    for string in strArr:
        length = len(string)
        
        if length not in group:
            group[length] = 1
        else:
            group[length] += 1
    
    print(group)
    
    return max(group.values())