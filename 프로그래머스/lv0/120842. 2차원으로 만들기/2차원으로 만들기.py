def solution(num_list, n):
    answer = []
    
    # [1, 2], [3, 4], [5, 6], [7, 8]
    for i in range(0, len(num_list), n):
        temp = []
        for j in range(i,i+n):
            temp.append(num_list[j])
        answer.append(temp)
    print(answer)
        
    
    
    return answer