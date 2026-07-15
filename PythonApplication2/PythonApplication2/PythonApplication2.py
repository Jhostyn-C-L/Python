import math

class Esfera:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 4 * math.pi * (self.radio ** 2)

    def volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)

    def diametro(self):
        return 2 * self.radio

radio = float(input("Introduzca el radio de la esfera para calcular sus valores: "))

esfera = Esfera(radio)

print(f"El area de su superficie es: {esfera.area():.2f}")
print(f"Su volumen es: {esfera.volumen():.2f}")
print(f"Su diametro es: {esfera.diametro():.2f}")