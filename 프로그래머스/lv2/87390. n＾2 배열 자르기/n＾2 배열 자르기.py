# def solution(n, left, right):
#     answer = []
    
#     arry = []
    
#     for i in range(n):
#         for j in range(n):
#             arry.append(max(i+1,j+1))
            
#     answer = arry[left:right+1]
    
#     return answer

# def solution(n, left, right):
#     answer = []
    
#     for i in range(left, right + 1):
#         answer.append(max(i // n, i % n) + 1)
        
#     return answer

def solution(n, left, right):
    return [max((i//n) + 1, (i%n) + 1) for i in range(left, right+1)]