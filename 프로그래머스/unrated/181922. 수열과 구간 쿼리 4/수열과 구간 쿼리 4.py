def solution(arr, queries):  
    for query in queries:
        index_arr = [num for num in range(query[0], query[1]+1)]
        for i, num in enumerate(arr):
            if i in index_arr and i%query[2] == 0:
                arr[i] += 1 
    return arr