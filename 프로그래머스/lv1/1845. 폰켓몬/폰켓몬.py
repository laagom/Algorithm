def solution(nums):
    pocket_dict = dict()
    qty = len(nums)//2 # 선택할 수 있는 포켓몬 종류
    
    # 연구실 포켓몬 분류
    for num in nums:
        # pocket_dict에 있으면 count++
        if num in pocket_dict.keys():
            pocket_dict[num] += 1
        else:
            # pocket_dict에 없으면 count 1
            pocket_dict[num] = 1
    
    # pocket_dict의 포켓몬 종류
    num_kind = len(pocket_dict.keys())
    
    # 선택할 수 있는 수가 포켓몬의 종류보다 적다면 그 수만큼만 그렇지 않으면 포켓몬 종류 수
    return qty if qty <= num_kind else num_kind