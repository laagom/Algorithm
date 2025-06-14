def solution(num_list):
    evenCnt = sum(1 for n in num_list if n%2 == 0);
    oddCnt = len(num_list) - evenCnt;
    return [evenCnt,oddCnt]