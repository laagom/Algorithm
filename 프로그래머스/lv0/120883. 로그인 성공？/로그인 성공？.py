def solution(id_pw, db):
    answer = ''
    
    temp = [0]*3
    
    for id, pwd in db:
        if id == id_pw[0] and pwd == id_pw[1]:
            temp[0] += 1
        
        if id == id_pw[0] and pwd != id_pw[1]:
            temp[1] += 1
        
        if id != id_pw[0] and pwd != id_pw[1]:
            temp[2] += 1
            
    if temp[0] > 0:
        answer = 'login'
    elif temp[1] > 0:
        answer = 'wrong pw'
    else:
        answer = 'fail'
    
    return answer