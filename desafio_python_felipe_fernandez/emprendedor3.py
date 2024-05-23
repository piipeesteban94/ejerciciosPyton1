print("Calculadora de utilidades actuales vs años anteriores\n")
p = int(input("Ingrese precio de la suscripción: "))
u = int(input("Ingrese cantidad de usuarios: "))
gt = int(input("Ingrese el gasto total: "))
utilidad_anterior = int(input("Ingresa utilidad del año anterior: "))

utilidades = p * u - gt
razon = round((utilidades / utilidad_anterior), 2)
print(f"Las utilidades actuales son: $ {utilidades}, las utilidades del año anterior fueron: ${utilidad_anterior}, por lo cual, la razon actual y la del año anterior es {razon}")