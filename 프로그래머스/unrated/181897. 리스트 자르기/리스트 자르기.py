def solution(n, slicer, num_list):
    answer = []
    a, b, c = slicer
    
    
    if n == 1:
        print(num_list[:b+1])
        return num_list[:b+1]
    if n == 2:
        print(num_list[a:])
        return num_list[a:]
    if n == 3:
        print(num_list[a:b+1])
        return num_list[a:b+1]
    if n == 4:
        print(num_list[a:b+1:c])
        return num_list[a:b+1:c]
    
n = 4
slicer = [1, 4, 2]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(solution(n, slicer, num_list))