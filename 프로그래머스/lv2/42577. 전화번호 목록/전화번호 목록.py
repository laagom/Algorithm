def solution(phone_book):
    # 전화번호부를 오름차순으로 정렬
    phone_book.sort()
    
    # loop를 돌리며 index, index+1을 비교하여 포함된 경우 False
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1].startswith(phone_book[i]):
                return False
            
    # 위의 로직을 통과 하면 그대로 True
    return True