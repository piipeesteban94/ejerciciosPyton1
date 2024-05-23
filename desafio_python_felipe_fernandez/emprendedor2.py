print("Calculadora de utilidades premium (50% adicional en la suscripcion)\n")
p = int(input("Ingrese precio de la suscripción: "))
u = int(input("Ingrese cantidad de usuarios normales: "))
up = int(input("ingrese cantidad de usuarios premium: "))
gt = int(input("Ingrese el gasto total: "))

utilidades = (p * u) + (up*(p * 1.5)) - gt
print("Las utilidades declaradas son: $", utilidades)