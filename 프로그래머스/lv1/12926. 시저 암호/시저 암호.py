def solution(s, n):
    answer = ''
    for char in s:
        unit_num = ord(char)   
        for _ in range(n):
            unit_num += 1
            if unit_num == ord("z") + 1:
                unit_num = ord("a")
            elif unit_num == ord("Z") + 1:
                unit_num = ord("A")
                
        if char == " ":
            answer += " "
        else:
            answer += chr(unit_num)     
    return answer