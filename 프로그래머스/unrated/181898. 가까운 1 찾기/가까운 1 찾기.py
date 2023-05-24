def solution(arr, idx):
    for i, num in enumerate(arr):
        if i >= idx and num == 1:
            return i
    return -1