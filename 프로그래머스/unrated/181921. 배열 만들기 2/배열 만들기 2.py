def solution(l, r):

    result = []

    for i in range(l, r+1):
        # 5로 나누어 떨어지지 않으면 건너뜀
        if i % 5 != 0:
            continue

        # 숫자자리마다 0 또는 5인지 판별하기 위한 변수 ch
        ch = str(i) 
        # 0또는 5만 있으면 True
        is_zero_or_five = True

        # 숫자 전체를 돎
        for j in ch:
            # 만약 각 자리가 5또는 0이 아니라면
            if j != "5" and j != "0":            
                is_zero_or_five = False

        # True로 0,5만 있는 숫자라면 result에 더함
        if is_zero_or_five:
            result.append(i)

    # print(result)

    if not result:
        return [-1]
    return result