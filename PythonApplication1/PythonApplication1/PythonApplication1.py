def romanoadecimal(Parametro):
    romano = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    resultado = 0
    indice = 0
    
    while indice < len(Parametro):
        
        if indice + 1 < len(Parametro) and romano[Parametro[indice]] < romano[Parametro[indice + 1]]:
            resultado += romano[Parametro[indice + 1]] - romano[Parametro[indice]]
            indice += 2 
        else:
            resultado += romano[Parametro[indice]]
            indice += 1 
    return resultado

Inicio = input("Introduzca el numero romano para convertir a decimal: ").upper()
total = romanoadecimal(Inicio)
print("Convertido a decimal: ", total)