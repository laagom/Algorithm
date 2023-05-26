def solution(arr, query):
    for i, num in enumerate(query):
        if i%2 == 0:
            arr = arr[:num+1]
            # print(arr)
        else:
            arr = arr[num:]
            # print(arr)
    return arr

# def solution(arr, query):
#     answer = []
#     for i in range(len(query)):
#         if i%2==0:
#             arr=arr[0:arr[query[i]]+1]
#         else:
#             arr=arr[arr[query[i]]:]

#     return arr



arr = [5, 1, 0, 4, 3, 2, 6, 7]
query = [6, 4, 3]

print(f'res: {solution(arr, query)}')