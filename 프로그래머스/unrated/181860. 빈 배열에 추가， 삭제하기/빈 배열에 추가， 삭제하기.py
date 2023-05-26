def solution(arr, flag):
    answer = []
    for i, boolean in enumerate(flag):
        if boolean:
            answer += [arr[i]]*(arr[i]*2)
        else:
            for _ in range(arr[i]):
                del answer[-1]
    return answer