def solution(s):
    words = s.split(' ')
    print(words)
    words = [word[0].upper()+word[1:].lower() if word != "" and word[0].isalpha else word.lower() for word in words]
    return ' '.join(words) 

s = " 5ello 5my LADY"
print(solution(s))