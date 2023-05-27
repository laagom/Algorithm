from collections import Counter

def solution(s):
    s = Counter(s.lower()) 
    return s['p'] == s['y']