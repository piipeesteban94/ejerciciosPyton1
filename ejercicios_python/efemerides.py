efemerides = {'1 de Enero': 'Año Nuevo',
            '27 de Febrero': 'Terremoto en Chile',
            '8 de Marzo': 'Día de la Mujer',
            '21 de Mayo': 'Glorias Navales',
            '18 de Septiembre': 'Fiestas Patrias',
            '19 de Septiembre': 'Glorias del Ejercito',
            '25 de Diciembre': 'Navidad'}

efemerides_lower ={k.lower():v for k,v in efemerides.items()}

fecha = input("Ingrese una fecha: ").lower()

print(f"Efemerides: {efemerides_lower.get(fecha, "No hay nada en esa fecha")}")
