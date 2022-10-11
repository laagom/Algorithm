
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        # 너무 길어...
#         cnt = 0;
#         for j in range(1, i+1):
#             if i % j == 0:
#                 cnt +=1;
        
#         if cnt % 2 == 0:
#             answer += i	
#         else:
#             answer -= i
        answer += get_count(i)
            
    return answer	

def get_count(n):
    answer = len([j for j in range(1, n+1) if not n%j])
    return -n if answer%2 else n