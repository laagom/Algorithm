def solution(n, m):
    gcd = max([i for i in range(min(n,m), 0, -1) if n%i == 0 and m%i == 0])
            
    lcm = min([i for i in range(max(n,m), (n*m)+1) if i%n == 0 and i%m == 0])
            
    return [gcd, lcm]