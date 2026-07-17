from ast import While

terreno = input()
indices = []
regiones = []
total = 0
for i in range(len(terreno)):
    if terreno[i] == "\\":
        indices.append(i)
    elif terreno [i] == "/" and indices:
        inicio = indices.pop()
        area = i - inicio
        total += area

        while regiones and regiones[-1][0] > inicio:
            area += regiones.pop()[1]
        regiones.append((inicio, area))
print(total)
print(len(regiones), end="")
for region in regiones:
    print(" ", region[1], end="")
print()