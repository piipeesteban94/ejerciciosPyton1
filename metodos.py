#METODOS DE CADENA STRING

#1- .count(), cuanta el numero de veces que aparece un caracter alfanumerico.
print("Santana".count("a")) #entrega un 3 ya que el string tiene 3 "a".

#2- .upper() transfroma el string a mayusculas.
print("santana".upper()) #resulta en SANTANA.

#3- .lower() transforma el string a minuscula.
print("SANTANA".lower()) #resulta en santana.

#4- .title() permite colocar mayusculas solo a la primera letra de cada palabra.
print("carlos santana".title()) #resulta en Carlos Santana.

#5- len() permite contar el numero de caracteres en un string. esto no es un metodo, por lo que se debe incluir un string dentro de la funcion.
print(len("carlos santana")) #resulta en 14 

#6- join() permite unir muchos elementos separados por un string.
print(", ".join(["a" , "b" , "c"]))

#7- .replace() reemplaza una subcadena de una cadena por otra y la devuelve-
print("Hola mundo".replace("o","0")) #resulta en H0la mund0




