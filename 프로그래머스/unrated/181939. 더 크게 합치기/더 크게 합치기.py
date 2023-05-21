def solution(a, b):
    return calc(a, b)

def calc(a, b):
    pre = int(str(a) + str(b))
    late = int(str(b) + str(a))
    
    return pre if pre > late else late