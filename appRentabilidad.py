import math

print("Bienvenido a la app de rentabilidad \n")
print("Seleccione el modulo que desee \n")

print("1- Calculadora de utilidades basico")
print("2- Calculadora de utilidades con usuarios premium")
print("3- Calculadora de utlidades actuales vs utilidades años anteriores \n")

menu_principal = input("Escriba un numero a eleccion del menu a utlizar: ")

if menu_principal == "1":
    print("¡Haz seleccionado la calculadora de utilidades basico!\n")
    p = int(input("Ingrese precio de la suscripción: "))
    u = int(input("Ingrese cantidad de usuarios: "))
    gt = int(input("Ingrese el gasto total: "))

    utilidades = p * u -gt
    print("Las utilidades declaradas son: $", utilidades)

elif menu_principal == "2":
    print("¡Haz seleccionado la calculadora de utilidades premium (50% adicional en la suscripcion)!\n")
    p = int(input("Ingrese precio de la suscripción: "))
    u = int(input("Ingrese cantidad de usuarios normales: "))
    up = int(input("ingrese cantidad de usuarios premium: "))
    gt = int(input("Ingrese el gasto total: "))

    utilidades = (p * u) + (up*(p * 1.5)) - gt
    print("Las utilidades declaradas son: $", utilidades)

elif menu_principal == "3":
    print("¡Haz seleccionado la calculadora de utilidades basico!")
    p = int(input("Ingrese precio de la suscripción: "))
    u = int(input("Ingrese cantidad de usuarios: "))
    gt = int(input("Ingrese el gasto total: "))
    utilidad_anterior = int(input("Ingresa utilidad del año anterior: "))

    utilidades = p * u - gt
    razon = round((utilidades / utilidad_anterior), 2)
    print(f"Las utilidades actuales son: $ {utilidades}, las utilidades del año anterior fueron: ${utilidad_anterior}, por lo cual, la razon actual y la del año anterior es {razon}")