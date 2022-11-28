from collections import defaultdict
def make_primes(n:int)->list:
    primes = [True] * (n + 1)
    primes[0:2] = [False, False]
    for num in range(2, int(n * 0.5) + 1):
        if primes[num]:
            for i in range(num ** 2, n + 1, num):
                primes[i] = False
    return primes

def make_prime_factorization(n):
    primes = make_primes(n)
    prime_numbers = [x for x in range(2, n + 1) if primes[x]]
    result = defaultdict(int)
    for number in prime_numbers:
        while n % number == 0 and n > 1:
            result[number] += 1
            n //= number
        if n == 1:
            break
    return result

def solution(a, b):
    numerator = make_prime_factorization(a)
    denominator = make_prime_factorization(b)

    # 분모 약분
    for key, value in numerator.items():
        if key in denominator:
            denominator[key] = max(0, denominator[key] - value)

    # 유한 소수 판별
    for key, value in denominator.items():
        if key == 2 or key == 5:
            continue
        if value > 0:
            return 2
    return 1