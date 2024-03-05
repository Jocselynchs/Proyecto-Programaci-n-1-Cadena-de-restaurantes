"""Cadena de restaurantes Sabores Deliciosos"""
""" Primer avance; Generar el primer módulo completo y funcional.
• Generar el segundo módulo completo y funcional.
• Generar el tercer módulo completo y funcional"""

print("Bienvenido a la cadena de restaurantes Sabores Deliciosos")
yes=True
no=False
counter=0
login=input("¿Desea ingresar al menu?\n Marque Si para ingresar al menu o No para salir del menu: ")
for i in range(login=="si"):
    print("Este es su menu")
    print("1.Registrar nueva sede")
    print("2.Modulo de registro de clientes")
    print("3.Modulo de reservaciones del restaurante")
    print("4.Modulo de toma de ordenes y pedidos")
    print("5.Modulo de resgistro de alimentos y bebidas")
    print("6.Modulo de facturacion")
    print("7.Salir.")
    option=int(input("Seleccione una opcion: "))
    if option==1:
        print("Usted selecciono la opcion:\n1.Registrar nueva sede")
    elif option == 2:
        print("Usted selecciono la opcion:\n2.Modulo de registro de clientes\n")
        while True:
            name = str(input('Ingrese su nombre: '))
            country = str(input('Ingrese su pais: '))
            province = str(input('Ingrese su provincia: '))
            canton = str(input('Ingrese su canton: '))
            district = str(input('Ingrese su distrito: '))
            address = str(input('Ingrese su direccion: '))

            if name.isdigit or country.isdigit or province.isdigit or canton.isdigit or district.isdigit or address.isdigit:
                print('¡Error! Verifique que los datos sean correctos\n')
                continue
        
            try:
                age = int(input('Ingrese su edad: '))
                ID = int(input('Ingrese su numero de identificacion: '))

                if not name or not country or not province or not canton or not district \
                    or not address or not age or not ID:
                    print('¡Error! Debe rellenar todo lo solicitado\n')
                    continue
                
                print('\nTipos de pago:')
                for wayToPay in ['• Efectivo', '• Transferencia', '• Tarjeta de credito']:
                    print(wayToPay)
                choice = str(input('\nElija su forma de pago: '))
                if choice not in ['efectivo', 'transferencia', 'tarjeta de credito']:
                    print('¡Error, eleccion de forma de pago no valida!\n')
                    continue

                break

            except ValueError:
                print('¡Verifique que no haya ingresado incorrectamente los datos!\n')
                continue

    elif option == 3:
        print("Usted selecciono la opción:\n3.Modulo e reservaciones del restaurante")
    elif option == 4:
        print("Usted selecciono la opcion:\n4.Modulo de toma de ordenes y pedidos")
    elif option == 5:
        print("Usted selecciono la opcion:\n5.Modulo de resgistro de alimentos y bebidas")
    elif option == 6:
        print("Usted selecciono la opcion:\n6.Modulo de facturacion")
    elif option == 7:
        print("Usted selecciono la opcion:\n7.Salir")
    elif login=="no":
        print("Usted salio del menu")
    else:
        print("Ingrese una opcion valida")

