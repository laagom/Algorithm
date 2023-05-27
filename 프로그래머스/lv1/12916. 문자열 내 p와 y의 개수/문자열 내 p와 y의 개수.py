def solution(s):
    s = s.lower()
    
    return True if ('p' not in s and 'y' not in s) or (s.count('p') == s.count('y')) else False
