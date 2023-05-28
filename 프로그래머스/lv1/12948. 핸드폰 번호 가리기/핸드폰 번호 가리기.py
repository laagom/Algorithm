def solution(phone_number):
    answer = ''
    for i, num in enumerate(phone_number):
        answer += "*" if i < len(phone_number)-4 else num
    return answer