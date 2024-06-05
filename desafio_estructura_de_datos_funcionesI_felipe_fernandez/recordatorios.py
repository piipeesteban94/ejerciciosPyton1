recordatorios = [
            ['2021-01-01', "11:00", "Levantarse y ejercitar"],
            ['2021-05-01', "15:00", "No trabajar"],
            ['2021-07-15', "13:00", "No hacer nada es feriado"],
            ['2021-09-18', "16:00", "Ramadas"],
            ['2021-12-25', "00:00", "Navidad"]
                 ]

#Agregar evento de empezar el año
recordatorios.insert(1, ['2021-01-02', '06:00', 'Empezar el año'])

#Editar evento del dia del trabajo
recordatorios[3][0] = '2021-07-16'

#Eliminar evento del dia del trabajo
del recordatorios[2]

# Agregar cena navidad y cena de año nuevo
recordatorios.insert(4, ['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo']) 

for recordatorio in recordatorios:
    print(recordatorio)