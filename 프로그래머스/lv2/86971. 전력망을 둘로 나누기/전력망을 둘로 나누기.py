# 6번. 전력망을 둘로 나누기

def count_child(node): 
    visited[node] = True  
    for n in graph[node]: 
        if not visited[n]:
            # print('node', node, 'li[node]',li[node])
            li[node] += count_child(n) + li[n]
    print(li,visited, node)
    return 1

def solution(n, wires):
    global visited, graph, li

    answer = n
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    li = [0] * (n + 1)

    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])

    count_child(1)
    print(li)

    for i in li: 
        answer = min(answer, abs(n - (i + 1) - (i + 1)))
                      
    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])