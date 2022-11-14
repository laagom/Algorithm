def solution(rsp):
    answer = ''
    array = {"2" : "0", "0" : "5", "5" : "2"}
    
    for r in rsp:
        answer += array[r]

    return answer