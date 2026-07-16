def binarySearch(A, T):
    L = 0
    R = len(A) - 1
    while L <= R:
        m = (L + R) // 2
        if A[m] < T:
            L = m + 1
        elif A[m] > T:
            R = m - 1
        else:
            return m
    return "unsuccessful"

Entrada = input("Introduzca los números ordenados, separados por espacios: ")
Listado = [int(x) for x in Entrada.split()]
T = int(input("Introduzca el número que quiere buscar: "))

Resultado = binarySearch(Listado, T)
if Resultado == "unsuccessful":
    print("Resultado: unsuccessful, el número no fue encontrado")
else:
    print(f"El número {T} se encuentra en la posición: {Resultado}")
