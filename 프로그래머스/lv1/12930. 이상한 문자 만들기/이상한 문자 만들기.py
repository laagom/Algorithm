def solution(s):
    result = []
    words = s.split(' ')
    for word in words:
        string = ""
        for i, char in enumerate(word):
            if i%2 == 0:
                string += char.upper()
            else:
                string += char.lower()
        result.append(string)
    return ' '.join(result)