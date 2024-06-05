import sys

soles_peru = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
peso_chileno = int(sys.argv[4])
print(f'''
    Los ${peso_chileno} pesos equivalen a:
    ${round(peso_chileno * soles_peru)} Soles
    ${round(peso_chileno * peso_argentino)} Pesos Argentinos
    ${round(peso_chileno * dolar_americano)} Dolares
    ''')