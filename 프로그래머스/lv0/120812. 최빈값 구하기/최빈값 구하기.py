def solution(array):
    answer = [ 0 for _ in range(max(array)+1)]
    
    print(answer)
    for num in array:
        answer[num] += 1
        
    print(answer)
    print(max(answer))
    print(answer.count(max(answer)))
    print(answer.index(max(answer)))

    if answer.count(max(answer)) == 1:
        return answer.index(max(answer))
    else:
        return -1
    # return answer