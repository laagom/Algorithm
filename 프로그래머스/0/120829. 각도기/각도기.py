def solution(angle):
    if angle <= 90:
        return 1 if angle < 90 else 2 # 예각 & 직각
    else:
        return 3 if angle < 180 else 4 # 둔각 & 평각