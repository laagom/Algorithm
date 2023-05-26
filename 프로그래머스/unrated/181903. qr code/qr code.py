def solution(q, r, code):
    #  내 풀이     
    # return ''.join(char for i, char in enumerate(code) if int(i%q) == r)
    
    # 남 풀이
    return code[r::q]