import sys

nombre_archivo = sys.argv[1]   
with open("lorem_ipsum.txt", 'r') as file:
    texto = file.read()

#numero de caracteres distintos:
caracteres = set([letra for letra in texto])
print(f"En numero de caracteres distintos es: {len(caracteres)}")
   
#numero de palabras distintas:
distinto = list(set(texto.split(" ")))
num_palabras = len(distinto)
print(f"El numero de palabras distintas es: {num_palabras}")
