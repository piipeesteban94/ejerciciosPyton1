import math

print("Calcular la velocidad de escape: \n")

gravedad = float(input("Ingrese la constante G: "))
radius = float(input("Ingrese el radio en kilometros: ")) * 1000

resultado = math.sqrt(2 * gravedad * radius)
print("La velocidad de escape es " , math.ceil(resultado), " [m/s]")