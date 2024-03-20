"""Cadena de restaurantes Sabores Deliciosos"""

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
    print('Sedes:')
    choseCampus = ['• San Rafael', '• Santo Domingo', '• Heredia', '• San Jose', '• Escazu']
    for x in choseCampus:
        print(x)
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
    day = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    print("El día de su reserva es", booking_day)
    available_day = False
    for i in day:
        if booking_day.lower() == i:
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
        

daysList = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
campusList = ['san rafael', 'santo domingo', 'heredia', 'san jose', 'escazu']
def option3(name, country, province, canton, district, address, age, ID):
    print("\nUsted selecciono la opción:\n3.Reservaciones del restaurante")
    while True:
            print('• Identificacion del cliente:')
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
    dayAvailable = False
    while not dayAvailable:
        day = input('Ingrese el dia de la semana que desea hacer la reserva: ')
        if day in daysList:
            dayAvailable = True
        else:
            print('El dia seleccionado no esta disponible. \nSeleccione otro dia.')
    
    campusAvailable = False
    while not campusAvailable:
        campus = input('Seleccione la sede para la reserva: ')
        if campus in campusList:
            campusAvailable = True
        else:
            print('La sede no esta disponible. \nSeleccione otra sede.')
    
    
    amountTables = int(input('Ingrese la cantidad de mesas para reserva: '))
    amountPeople = int(input('Ingrese la cantidad de personas para reserva: '))

    while amountTables <= 0 or amountPeople <= 0:
        print('¡Error! Verifique las mesas o personas')
        amountTables = int(input('Ingrese la cantidad de mesas para reserva: '))
        amountPeople = int(input('Ingrese la cantidad de personas para reserva: '))
        
        if amountTables >= 0 and amountPeople >= 0:
            break
    

def option4():
    print("\nUsted selecciono la opcion:\n4.Toma de ordenes y pedidos")
    print("Este es el menu digital para la toma de ordenes y pedidos")
    order_menu="Este es el menu para ordenar pedidos"
    
    def take_orders():
        available_dishes = ["Pollo Asado", "Pescado Frito", "Ensalada César", "Hamburguesa con Queso", "Pasta Alfredo"]
        available_drinks = ["Bebida natural", "Gaseosa"]
        available_desserts = ["cheesecake", "Helado", "Pastel de chocolate"]
        tables = 15
        available_tables = ["Disponible"] * tables
        order = [[] for _ in range(tables)]
        print("Por favor rellene los siguientes espacios para realizar el pedido")
        verify_order = True
        
        while verify_order:
            table_selection = int(input("Ingrese el número de mesa (1-15): ")) - 1
            if not (0<=table_selection and table_selection<tables):
                print("El número de mesa no está disponible") 
                return
            if available_tables[table_selection] != "Disponible":
                print("La mesa", table_selection + 1, "ya está ocupada por", available_tables[table_selection])
            else:
                available_tables[table_selection] = input("Ingrese el nombre del cliente a facturar: ")
                print("platos disponibles: \n 1.Pollo Asado\n 2.Pescado Frito\n 3.Ensalada César\n 4.Hamburguesa con Queso\n 5.Pasta Alfredo\n")
                dish = input("Ingrese el platillo a solicitar: ")
                print("bebidas disponibles: \n 1.Bebida natural\n 2.Gaseosa\n")
                drink = input("Ingrese la bebida: ")
                print("Postres disponibles: \n 1.cheesecake\n 2.Helado\n 3.Pastel de chocolate\n")
                dessert = input("Ingrese el postre a solicitar: ")

                if dish.lower() in [dish.lower() for dish in available_dishes]:
                    print("El platillo está disponible")
                else:
                    print("No se encuentra disponible")
                if drink.lower() in [drink.lower() for drink in available_drinks]:
                    print("La bebida está disponible")
                else:
                    print("No se encuentra disponible")
                if dessert.lower() in [dessert.lower() for dessert in available_desserts]:
                    print("El postre está disponible")
                else:
                    print("No se encuentra disponible")
                    
                amount_dish = int(input("Ingrese la cantidad de " + dish + " que desea solicitar: "))
                amount_drinks = int(input("Ingrese la cantidad de " + drink + " que desea solicitar: "))
                amount_dessert = int(input("Ingrese la cantidad de " + dessert + " que desea solicitar: "))
                dish_status = "Pedido Recibido"
                dish_order = [dish, amount_dish, drink, amount_drinks, dessert, amount_dessert, dish_status]
                order[table_selection] = dish_order
                print("El pedido se realizó con éxito, pronto estará listo")
                kitchen_send = input("¿Enviar pedido a la cocina? (si/no): ")
                
                if kitchen_send.lower() == "si":
                    order[table_selection][-1] = "En preparación"
                    print("El pedido está siendo preparado")
                    order_continue = input("¿Desea realizar otro pedido? (si/no): ")
                if order_continue.lower() == "no":
                    verify_order = False

    take_orders()

def option5():
    print("\nUsted selecciono la opcion:\n5.Resgistro de alimentos y bebidas")
    catalogue = []
    while True:
        print("\n1. Agregar producto")
        print("2. Mostrar catalogo")
        print("3. Salir")
        select_option = int(input("Seleccione una opcion: "))

        if select_option == 1:
            print("Ingrese los detalles del producto:")
            name = input("Nombre: ")
            description = input("Descripcion: ")
            category = input("Categoria: ")
            price = float(input("Precio: "))
            product = [name, description, category, price]
            catalogue=catalogue+[product]
            print("¡Producto agregado al catalogo!")

        elif select_option == 2:
            if not catalogue:
                print("El catalogo esta vacio.")
            else:
                print("Catalogo de productos:")
                for product in catalogue:
                    print("Nombre:", product[0])
                    print("Descripcion:", product[1])
                    print("Categoria:", product[2])
                    print("Precio:", product[3])
                    print()

        elif select_option == 3:
            print("Salir")
            break

        else:
            print("Opcion invalida")

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


