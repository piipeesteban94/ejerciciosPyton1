#imprimir hola mundo
print("hola mundo")

#escribir un programa que almacene la cadena hola mundo en una variable y luego muestre por pantalla el contenido de la variable.
variable1 = "Hola mundo"
print(variable1)

#escribir un programa que muestre por pantalla el resultado de una operacion
suma = 3+2
multi = 2*5
divi = (suma / multi)
result = (divi ** 2)
print("el resultado es: ", result)

#escribir un programa que pregunte el nombre del usuario en la consola y despues que el usuario lo introduzca muestre por pantalla
#hola <nombre> donde <nombre> es el nombre que el usuario introdujo

nombre =  input("introduce tu nombre: ")
print("hola " + nombre)

# escribir un programa que le pida al usuario la cantidad de horas y el valor de cada hora para dar resultado el total ganado por esas horas

horas = float(input("introduce la cantidad de horas trabajadas: "))
valor = float(input("introduce el valor por hora de trabajo: "))
result = valor * horas
print("el valor total ganado por las " , horas ," trabajadas es: " ,result)

# escribir un programa que lea un entero positivo n, introducido por el usuario despues muestre en pantalla la suma de todos los enteros desde 1 hasta n,
# la suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma = n(n+1)/2

n = int(input("ingrese un numero entero positivo: "))
suma = n + 1
multi = n * suma
result = multi / 2

print("el resultado de tu numero entero en la ecuacion es: ", result)
