import sys

print("### Calculadora de IMC según la OMS ###\n")

peso =  int(sys.argv[1])
altura = int(sys.argv[2])

altura = altura / 100
imc = (peso / (altura)**2)

if imc < 18.5:
    print(f"Su IMC es {imc:.2f}")
    print(f"La clasificación OMS es bajo peso.")

elif 18.5 <= imc < 25:
    print(f"Su IMC es {imc:.2f}")
    print(f"La clasificación OMS es de peso adecuado.")

elif 25 <= imc < 30:
    print(f"Su IMC es {imc:.2f}")
    print(f"La clasificación OMS es de sobrepeso.")

elif 30 <= imc < 35:
    print(f"Su IMC es {imc:.2f}")
    print(f"La clasificación OMS es de obesidad grado I")

elif 36 <= imc < 40:
    print(f"Su IMC es {imc:.2f}")
    print(f"La clasificación OMS es de obesidad grado II")

else:
    print(f"Su IMC es {imc:.2f}")
    print(f"La clasificación OMS es de obesidad grado III.")


