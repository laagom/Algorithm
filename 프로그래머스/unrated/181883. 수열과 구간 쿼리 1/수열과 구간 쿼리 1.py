def solution(arr, queries):
    for query in queries:
        s, e = query[0], query[1]
        for i, num in enumerate(arr):
            if i in range(s, e+1):
                arr[i] += 1
    return arr