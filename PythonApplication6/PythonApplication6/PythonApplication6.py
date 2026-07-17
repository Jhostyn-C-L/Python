tarjeta, K = input().split()
K = int(K)

grupos = []

for i in range(0, 16, 4):
    grupos.append(tarjeta[i:i+4][::-1])
K = K % 4

for i in range(K):
    ultimo = grupos.pop()
    grupos.insert(0, ultimo)
Total = "".join(grupos)
print(Total)

if Total != tarjeta:
    print("SI")
else:
    print("NO")
