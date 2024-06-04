estimulos = input('¿Responde a estímulo? (si / no): ')
if estimulos.lower() == 'si':
    print('Valorar la necesidad de llevarlo al hospital más cercano')
else:
    print('Debe abrir la vía Aérea')
    respira = input('¿Respira? (si / no): ')
    if respira.lower() =='si':
        print('Permitirle posición de suficiente ventilación')
    else:
        print('Administrar 5 Ventilaciones y llamar a Ambulancia')
        llego_ambulancia = False
        while llego_ambulancia == False:
            signos_vida = input('¿Signos de vida?  (si / no): ')
            if signos_vida.lower() == 'si':
                print('Reevaluar a la espera de la ambulancia')
            else:
                print('Administrar compresiones torácicas hasta que llegue la ambulancia')
                llego_ambulancia = input('¿Llegó ambulancia? (si /no): ')
                if llego_ambulancia.lower() == 'si':
                    llego_ambulancia = True
                else:
                    llego_ambulancia = False
    print('FIN')
