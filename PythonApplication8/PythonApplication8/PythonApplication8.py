C = int(input())
for i in range(C):
    T, PPEQ, PGDE, MPEQ, MGDE = map(int, input().split())
    mejor = 0
    max_grandes = T // MGDE
    for grandes in range(max_grandes + 1):
        tiempo_restante = T - grandes * MGDE
        pequeños = tiempo_restante // MPEQ
        dinero = grandes * PGDE + pequeños * PPEQ
        if dinero > mejor:
            mejor = dinero
    print(mejor)

