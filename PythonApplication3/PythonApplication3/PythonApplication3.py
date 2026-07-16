def insertionSort(A):
    i = 1
    while i < len(A):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j], A[j-1] = A[j-1], A[j]
            j = j - 1
        i = i + 1
    return A

Entrada = input("Introduzca los números para ordenarlos de menor a mayor(recuerde separarlos por espacios los números): ")
Listado = [int(x) for x in Entrada.split()]

print("Listado original: ", Listado)
print("Listado organizado: ", insertionSort(Listado))