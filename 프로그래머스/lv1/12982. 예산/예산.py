# def solution(d, budget):
#     budget_limit = 0
#     dept = []
    
#     d = sorted(d)
#     for num in d:
#         budget_limit += num
#         dept.append(num)
#         if budget_limit > budget:
#             budget_limit -= num
#             dept.pop()
#     return len(dept)

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)