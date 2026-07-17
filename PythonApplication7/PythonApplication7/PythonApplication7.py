A, B = map(int, input().split())
A = abs(A)
B = abs(B)

while B != 0:
    A, B = B, A % B
print(A)