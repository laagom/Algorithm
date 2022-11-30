def solution(common):
    answer = 0
    
    num = common[1]-common[0]
    print(num)
    
    if common[1] + num == common[2]:
        return common[-1] + num
    else:
        return common[-1] * common[1]//common[0]
 