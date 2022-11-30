def solution(num, total):
    answer = []
    
    middleNum = total // num
    subtracNum = num // 2 if total % num == 0 else num // 2 -1
    
    startNum = middleNum - subtracNum
    
    for i in range(0, num):
        answer.append(startNum + i)
    
    return answer

