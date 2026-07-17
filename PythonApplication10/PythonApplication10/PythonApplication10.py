N = int(input())
vocales = "AEIOU"
fuertes = "AEO"

for i in range(N):
    palabra = input()
    hiato = False
    diptongo = False

    for j in range(len(palabra) - 1):
        a = palabra[j]
        b = palabra[j + 1]
        if a in vocales and b in vocales:
            if (a in fuertes and b in fuertes) or (a == b and a in "IU"):
                hiato = True
            else:
                diptongo = True
    if hiato and diptongo:
        print("AMBOS")
    elif hiato:
        print("HIATO")
    elif diptongo:
        print("DIPTONGO")
    else:
        print("NINGUNO")