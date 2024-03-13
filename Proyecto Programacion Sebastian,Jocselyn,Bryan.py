"""Cadena de restaurantes Sabores Deliciosos"""
""" Primer avance; primer módulo completo y funcional.
• segundo módulo completo y funcional.
• tercer módulo completo y funcional"""

print("Bienvenido a la cadena de restaurantes Sabores Deliciosos")
login = input("¿Desea ingresar al menu?\n Marque Si para ingresar al menu o No para salir del menu: ")

def principal_menu():
    print("\nEste es su menu:")
    print("1.Registrar nueva sede")
    print("2.Registro de clientes")
    print("3.Reservaciones del restaurante")
    print("4.Toma de ordenes y pedidos")
    print("5.Resgistro de alimentos y bebidas")
    print("6.Facturacion")
    print("7.Salir.")


def option1():
    print("\nUsted selecciono la opcion:\n1.Registrar nueva sede")
    application_campus = input("Ingrese el nombre de la sede: ")
    print("***La capacidad total de la sede", application_campus,
          "es de 15 mesas,\n para una capacidad de 4 personas como máximo por mesa, para un total de 60 personas en el restaurante***")
    
    number_clients=int(input("Ingrese la cantidad de comensales para ordenar: "))
    if number_clients > 0:
        number_tables = 15
        maximum_capacity = 4
        tables_needed = (number_clients + maximum_capacity - 1) // maximum_capacity
        available_tables = number_tables - tables_needed
        print("La cantidad de mesas para reservar es de: ", number_tables,
              "\n""la cantidad de mesas disponible es de ", available_tables)
    
    print("Días para reservar:")
    print(" **Lunes** \n **Martes**\n **Miércoles**\n **Jueves**\n **Viernes**\n **Sábado**\n **Domingo**")
    booking_day = input("Ingrese el día de la semana que desee hacer su reserva: ")
    day = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    print("El día de su reserva es ", booking_day)
    available_day = False
    for i in day:
        if booking_day == i:
            available_day = True
    if available_day:
        print("El día está disponible")
    else:
        print("El día No está disponible")



def option2():
    global name
    global country
    global province
    global canton
    global district
    global address
    global age
    global ID

    print("\nUsted selecciono la opcion:\n2.Registro de clientes")
    while True:
            name = str(input('Ingrese su nombre: '))
            country = str(input('Ingrese su pais: '))
            province = str(input('Ingrese su provincia: '))
            canton = str(input('Ingrese su canton: '))
            district = str(input('Ingrese su distrito: '))
            address = str(input('Ingrese su direccion: '))


            try:
                age = int(input('Ingrese su edad: '))
                ID = int(input('Ingrese su numero de identificacion: '))
                if age < 0 or ID < 0:
                    print('¡Respuesta invalida! Verifique que la edad o el numero de identificacion sean correctos.\n')
                    continue
                elif not name or not country or not province or not canton or not district \
                    or not address or not age or not ID:
                    print('¡Error! Debe rellenar todo lo solicitado\n')
                    continue
                
                print('\nTipos de pago:')
                for wayToPay in ['• Efectivo', '• Transferencia', '• Tarjeta de credito']:
                    print(wayToPay)
                choice = str(input('\nElija su forma de pago: '))
                print('Usted ha elegido: ', choice.lower())
                if choice.lower() not in ['efectivo', 'transferencia', 'tarjeta de credito']:
                    print('¡Error, eleccion de forma de pago no valida!\n')
                    continue

                break

            except ValueError:
                print('¡Verifique que no haya ingresado incorrectamente los datos!\n')
                continue
        

def option3(name, country, province, canton, district, address, age, ID):
    print("\nUsted selecciono la opción:\n3.Reservaciones del restaurante")
    while True:
            print('\n• Identificacion del cliente:')
            name_Verication = str(input('Ingrese el nombre: '))
            country_Verication = str(input('Ingrese el pais: '))
            province_Verication = str(input('Ingrese la provincia: '))
            canton_Verication = str(input('Ingrese el canton: '))
            district_Verication = str(input('Ingrese el distrito: '))
            address_Verication = str(input('Ingrese la direccion: '))
            age_Verication = int(input('Ingrese la edad: '))
            ID_Verication = int(input('Ingrese el numero de identificacion: '))
            
            #Verificacion de cliente existente
            if name_Verication == name and country_Verication == country and province_Verication == province\
                and canton_Verication == canton and district_Verication == district and address_Verication == address\
                and age_Verication == age and ID_Verication == ID:
                print('El cliente si existe.')
            else: 
                print('El cliente no existe aun.')
            break

    print('• Datos para reserva:')    
    days = int(input('Dias deseados para la reserva: '))
    campus = str(input('Seleccione la sede para la reserva: ')) #Verificar despues
            
            #amountTables = int(input('Ingrese la cantidad de mesas para reserva: '))
            #amountPeople = int(input('Ingrese la cantidad de personas para reserva: '))
            
                
def option4():
    print("\nUsted selecciono la opcion:\n4.Toma de ordenes y pedidos")

def option5():
    print("\nUsted selecciono la opcion:\n5.Resgistro de alimentos y bebidas")

def option6():
    print("\nUsted selecciono la opcion:\n6.Facturacion")

while login.lower() == "si":
    principal_menu()
    option = int(input("Seleccione una opción: "))

    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        try: 
            option3(name, country, province, canton, district, address, age, ID)
        except NameError:
            print('¡No se ha registrado ningun cliente aun!')    
    elif option == 4:
        option4()
    elif option == 5:
        option5()
    elif option == 6:
        option6()
    elif option == 7:
        print("\nUsted selecciono la opcion:\n7.Salir")
        break
    else:
        print("Ingrese una opcion valida\n")
        continue



