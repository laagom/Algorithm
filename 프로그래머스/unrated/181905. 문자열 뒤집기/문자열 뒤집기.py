def solution(my_string, s, e):
    
    if e == 0:
        return my_string
    print(my_string[e:None if s == 0 else s-1:-1], 11)
    return my_string[:s] + my_string[e:None if s == 0 else s-1:-1] + my_string[e+1:]


my_string = "HelloMyMaster"
s, e = 0, 4


print(solution(my_string, s, e))