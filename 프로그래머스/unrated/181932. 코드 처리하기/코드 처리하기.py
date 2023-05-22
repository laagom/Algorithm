def solution(code):
    mode = 0
    ret = ""
    for i, char in enumerate(code):
        if mode == 0:
            if char != "1" and i%2 == 0: 
                ret += char
            elif char == "1":
                mode = 1
        else:
            if char != "1" and i%2 == 1:
                ret += char
            elif char == "1":
                mode = 0 
                
    return "EMPTY" if ret == "" else ret