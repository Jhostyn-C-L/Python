import math

C = int(input())
for i in range(C):
    N, B, K = map(int, input().split())
    g = math.gcd(N, K)
    m = N // g
    if B % m == 0:
        print(0)
    else:
        print(m - (B % m))