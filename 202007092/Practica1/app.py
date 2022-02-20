

from ast import Break, Continue

while True:
    print('''
---- Menú ----
1. Cargar Archivo data
2. Cargar archivo lfp
3. Analizar
4. Reportes
5. Salir
---- ---- ----
        ''')

    opt = input('Ingresa una opción: ')

    if opt =='1':
        print('cargar archivos data')
    elif opt =='2':
        print('Cargar archivos lfp')
    elif opt =='3':
        print('se analizo')
    elif opt == '4':
        print('se crearon reportes')
    elif opt =='5':
        print("saliendo...")
        break
    else: 
        print('no se que paso')
        continue
