n, D = map(int, input().split())
precios = list(map(int, input().split()))
mejor = D
for i in range(n):
    compra = precios[i]
    dolares = D // compra
    resto = D % compra

    venta = max(precios[i:])
    dinero = dolares * venta + resto
    if dinero > mejor:
        mejor = dinero

print(mejor)