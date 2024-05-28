import random
import sys

usuario = sys.argv[1]
usuario = usuario.lower() #cambia el string a minuscula
print(f'Tú jugaste {usuario}')

cpu = random.choice(['piedra', 'papel', 'tijeras'])
print(f'Computador eligió {cpu}')

#Evalucación usuario piedra
if usuario == 'piedra': 
	if cpu == 'piedra': 
		print('Empate: ambos elijeron piedra')
	elif cpu == 'papel':
		print('Perdiste!! papel gana a piedra')
	else: 
		print('Ganaste!!: piedra gana a tijera')

#Evalucación usuario papel
elif usuario == 'papel':
	if cpu == 'piedra': 
		print('Ganaste!!: papel gana a piedra')
	elif cpu == 'papel':
		print('Empate: ambos elijeron papel')
	else:
		print('Perdiste!! papel pierde con tijera')

#Evalucación usuario tijera
elif usuario == 'tijeras':
	if cpu == 'piedra': 
		print('Perdiste!! tijera pierde contra piedra')
	elif cpu == 'papel':
		print('Ganaste!!: tijeras corta el papel')
	else: 
		print('Empate: ambos elijieron tijeras')

#En caso de no ingresar un valor válido
else:
	print ('Argumento inválido: Debe ser piedra, papel o tijera.')