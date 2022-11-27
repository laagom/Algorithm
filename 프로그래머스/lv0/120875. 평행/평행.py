def solution(dots):
    # 두점의 기울기가 동일 한 값이 존재하면 1
    # 두점의 기울기가 동일 한 값이 없으면 0
    # 두점의 기울기 (x1, y1) (x2, y2)
    # 기울기 = (y2-y1)/(x2-x1)
    
    answer = 0
    leanArr = []
    
    for i in range(0, len(dots)):
        for j in range(i+1, len(dots)):
            
            m = (dots[i][1]-dots[j][1]) / (dots[i][0]-dots[j][0])
            
            if m in leanArr:
                return 1
            leanArr.append(m)
       
    return answer