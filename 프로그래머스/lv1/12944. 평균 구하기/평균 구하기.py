def solution(arr):
    # 분모가 0인 경우가 존재하면 안되기 때문에 조건 추가
    # 단, 제한사항에 arr의 길이가 최소 1이기 때문에 사실상 필요 없음
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)