from string import ascii_lowercase

password = input('Ingrese una contraseña: ')
cont = 0
for letra_password in password:
    for letra in ascii_lowercase:
        cont += 1
        if letra == letra_password:
            break
        
print(f'La contraseña fue forzada en {cont} intentos')
