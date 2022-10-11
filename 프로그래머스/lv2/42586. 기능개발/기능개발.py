from math import ceil

def solution(progresses, speeds):
    answer = []
    flag = 0
    
    # 일자 개선
    # date = [int((100 - progres) / speed) for progres, speed in zip(progresses, speeds)]
    date = [ceil((100 - progres) / speed) for progres, speed in zip(progresses, speeds)]
    
    print('date: {}'.format(date)) 
    
    for idx in range(len(date)):   
        if date[idx] > date[flag]:            
            answer.append(idx - flag)
            flag = idx
            
    answer.append(len(date) - flag)
 
    return answer