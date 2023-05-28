def solution(n):
    pre_bin = bin(n)[2:]
    n += 1
    while True:
        post_bin = bin(n)[2:]
        
        if str(pre_bin).count("1") == str(post_bin).count("1"):
            return n
        else:
            n += 1
    return answer