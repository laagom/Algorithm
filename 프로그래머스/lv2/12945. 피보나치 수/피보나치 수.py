def solution(n):
    FX = 0
    FY = 1
    for num in range(2, n+1):
        FX, FY = FY, (FX+FY)
        
    return FY%1234567

# 0, 1, 1, 2, 3, 5, 8, 13....