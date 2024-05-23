print("Calculadora de utilidades basico!\n")
p = int(input("Ingrese precio de la suscripción: "))
u = int(input("Ingrese cantidad de usuarios: "))
gt = int(input("Ingrese el gasto total: "))

utilidades = p * u -gt
print("Las utilidades declaradas son: $", utilidades)
