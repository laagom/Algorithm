# 4번. 카펫

def solution(brown, yellow):
    yellow_H = [h for h in range(1,int(yellow**0.5)+1)]
    yellow_W = [yellow/h for h in yellow_H]

    for YW, YH in zip(yellow_W, yellow_H):
        if (YW+2)*(YH+2) == (brown+yellow):
            return [YW+2, YH+2]

    answer = []

# solution(24,24)