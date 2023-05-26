# def solution(rank, attendance):
#     hash_map = {}
#     attend = []
    
#     for num, boolean in zip(rank, attendance):
#         if boolean:
#             hash_map[rank.index(num)] = num
    
#     sorted_hash = sorted(hash_map.items(), key=lambda x: x[1])
    
#     return 10000*sorted_hash[0][0] + 100*sorted_hash[1][0] + sorted_hash[2][0]

def solution(rank, attendance):
    arr = sorted([(x, i)for i, x in enumerate(rank) if attendance[i]])

    return 10000*arr[0][1]+100*arr[1][1]+arr[2][1]