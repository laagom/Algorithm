# 5번. 피로도

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    li_P = permutations(dungeons, len(dungeons))
    for dungeon in li_P:
        k_temp = k
        count = 0
        for d in dungeon:
            if k_temp >= d[0]:
                k_temp -= d[1]
                count += 1
        answer = max(answer, count)
    return answer

# 5번. 피로도 (dfs 활용 다른 사람의 풀이)

# def dfs(k, cnt, dungeons):
#     global answer 
#     # print(visited, k)
#     if cnt > answer:
#         answer = cnt
    
#     for i in range(len(dungeons)):
#         if not visited[i] and k >= dungeons[i][0]:
#             visited[i] = True
#             dfs(k - dungeons[i][1], cnt + 1, dungeons)
#             visited[i] = False
        
# def solution(k, dungeons):
#     global answer, visited
#     answer = 0
#     visited = [False] * len(dungeons)
#     dfs(k, 0, dungeons)
#     return answer

# solution(80, [[80,20],[50,40],[30,10]])