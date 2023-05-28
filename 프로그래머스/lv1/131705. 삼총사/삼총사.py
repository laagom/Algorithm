from itertools import combinations

def solution(number): 
    return len([three_member for three_member in combinations(number, 3) if sum(three_member) == 0])