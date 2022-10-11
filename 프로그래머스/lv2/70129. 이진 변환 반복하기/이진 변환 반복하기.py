
# def solution(s):    
#     cnt = 0
#     zero = 0
    
#     while s != "1":
        
#         zero += s.count("0")
#         s = s.replace("0","")
        
#         s = bin(len(s))[2:]       
#         cnt += 1     
        
#     return [cnt, zero]

def getBin(str):
    res = []
    while str != 0:
        if str % 2 == 1:
            res.append("1")
        else:
            res.append("0")
            
        str = str//2
    return "".join(res)

def solution(s):
    zero = 0
    count = 0

    while s != "1":    
        zero += s.count("0")
        
        s = s.replace("0","")        
        s = getBin(len(s))
        
        count += 1     
    answer = [count, zero]
    return answer