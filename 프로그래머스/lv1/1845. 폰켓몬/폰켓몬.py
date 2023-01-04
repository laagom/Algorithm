def solution(nums):
    answer      = 0
    pocket_dict = dict()
    qty         = len(nums)//2
    
    for num in nums:
        if num in pocket_dict.keys():
            pocket_dict[num] += 1
        else:
            pocket_dict[num] = 1
            
    num_mon = len(pocket_dict.keys())
    
    return qty if qty <= num_mon else num_mon