def solution(arr, k):
    num_list = []

    for i, num in enumerate(arr):
        if num not in num_list and len(num_list) < k:
            num_list.append(num)
    
    if len(num_list) < k:
        num_list += [-1]*(k-len(num_list))

    return num_list


arr = [5, 3, 1, 4, 2]
print(solution(arr, 3))