# def solution(array, commands):
#     answer = []
    
#     # 들어온 commands만큼 반복을 돌면서 
#     for i, command in enumerate(commands, start=1): 
#         # print(f'i : {i} and command : {command}')
#         # i~j까지 자르고 
#         # 나온 리스트를 정렬
#         sorted_array = sorted(array[command[0]-1:command[1]])
#         # print(f'sorted_array : {sorted_array} and command[2] : {command[2]}')
        
#         # k번째 있는 수 구해
#         # print(sorted_array[command[2]-1])
#         answer.append(sorted_array[command[2]-1])    
        
#     return answer


def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))