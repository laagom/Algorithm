def solution(arr, queries):
    answer = []
    for query in queries:
        temp_arr = arr[query[0]:query[1]+1]
        range_arr = [num for num in temp_arr if num > query[2]]
        
        if len(range_arr) > 0:
            answer.append(min(range_arr))
        else:
            answer.append(-1)
    return answer