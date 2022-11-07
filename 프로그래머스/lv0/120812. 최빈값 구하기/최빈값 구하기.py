def solution(array):
    answer = [ 0 for _ in range(max(array)+1)]
    
    for num in array:
        answer[num] += 1
    
    # 최빈값을 가지는 갯수가 1개이면 최빈값 반환
    if answer.count(max(answer)) == 1:
        return answer.index(max(answer))
    else:
        # 최빈값을 가지는 갯수가 1보다 크면 -1반환
        return -1