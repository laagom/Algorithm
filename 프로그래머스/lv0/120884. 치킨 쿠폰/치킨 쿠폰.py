def solution(chicken):
    service = 0
    while chicken >= 10:
        div, mod = divmod(chicken, 10)
        service += div
        chicken = div+mod
    return service