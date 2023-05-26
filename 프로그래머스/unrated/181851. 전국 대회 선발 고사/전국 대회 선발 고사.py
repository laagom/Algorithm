def solution(rank, attendance):
    hash_map = {}
    attend = []
    
    for num, boolean in zip(rank, attendance):
        if boolean:
            hash_map[rank.index(num)] = num
    
    sorted_hash = sorted(hash_map.items(), key=lambda x: x[1])
    
    return 10000*sorted_hash[0][0] + 100*sorted_hash[1][0] + sorted_hash[2][0]