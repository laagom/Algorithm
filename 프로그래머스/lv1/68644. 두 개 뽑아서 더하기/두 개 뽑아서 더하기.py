def solution(arry):
    res = []

    res = [arry[i]+arry[j] for i in range(len(arry) -1) for j in range(i+1, len(arry))]
    res = list(set(res))
    res.sort()
    return res