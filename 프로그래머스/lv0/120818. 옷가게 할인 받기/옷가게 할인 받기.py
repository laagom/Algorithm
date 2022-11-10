def solution(price: int) -> int:
    
    if price >= 500000:
        return int(price * 0.8)
    if price >= 300000:
        return int(price * 0.9)
    if price >= 100000:
        return int(price * 0.95)
    return price

if __name__ == '__main__':
    print(solution(150000))  # 142,500
    print(solution(580000))  # 464,000