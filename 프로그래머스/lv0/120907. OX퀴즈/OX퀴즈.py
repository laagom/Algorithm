def solution(quiz):
    answer = []
    
    for string in quiz:
        temp = list(string.split())
        print(list(string.split()))
        
        print(eval(temp[0]+temp[1]+temp[2]))
        if eval(temp[0]+temp[1]+temp[2]) == int(temp[4]):
            answer.append("O")
        else:
            answer.append("X")
    
    return answer