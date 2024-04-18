import os
"""Alumnos: Jocselyn chaves sevilla y sebastian fernandez hernandez """
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

availabilityList = [0,0,0,0,0,0]
def option2():
    global availabilityList
    global group
    file=open("pedidos.txt","w")

    print("\nUsted selecciono la opcion:\n2.Registro de clientes")
    while True:
            name = str(input('Ingrese su nombre: '))
            country = str(input('Ingrese su pais: '))
            province = str(input('Ingrese su provincia: '))
            canton = str(input('Ingrese su canton: '))
            district = str(input('Ingrese su distrito: '))
            address = str(input('Ingrese su direccion: '))
            if name and country and province and canton and district and address:
                group = [name, country, province, canton, district, address]
                availabilityList = availabilityList + [group]


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
    file.write("Cliente: "+ str(name) + '\n' + 'Metodo de pago: ' + str(choice)+'\n')
    file.close()


def option3(availabilityList, group):
    print("\nUsted selecciono la opción:\n3.Reservaciones del restaurante")
    while True:
        try: 
            print('• Identificacion del cliente')
            name_Verication = str(input('Ingrese el nombre: '))
            country_Verication = str(input('Ingrese el pais: '))
            province_Verication = str(input('Ingrese la provincia: '))
            canton_Verication = str(input('Ingrese el canton: '))
            district_Verication = str(input('Ingrese el distrito: '))
            address_Verication = str(input('Ingrese la direccion: '))
            age_Verication = int(input('Ingrese la edad: '))
            ID_Verication = int(input('Ingrese el numero de identificacion: '))
            
            #Verificacion de cliente existente
            if group in availabilityList:   
                print('El cliente si existe.')
            else: 
                print('El cliente no existe aun.')
            break
        
        except ValueError:
            print('Datos invalidos, verifique que sean correctos')
            continue

    print('• Datos para reserva:')  

    def availability():
        daysList = ["1.lunes", "2.martes", "3.miércoles", "4.jueves", "5.viernes", "6.sábado", "7.domingo"]
        campusList = ['1.san rafael', '2.santo domingo', '3.heredia', '4.san jose', '5.escazu']  
        tablesList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        days = 7
        campus = 5
        tables = 15
        availableDays = ['Disponible'] * len(daysList)
        availableCampus = ['Disponible'] * len(campusList)
        availableTables = ['Disponible'] * len(tablesList)

        print("Por favor rellene los siguientes espacios para realizar el pedido")
        verify_order0 = True
        
        #Seleccion de dias para reservar:
        while verify_order0:
            for i in daysList:
                print(i)
            try:
                daySelection = int(input('Ingrese el número de la semana para reservar: ')) - 1
                if daySelection < 0 or daySelection >= len(availableDays):
                    print("Selección inválida. Por favor, elija un número de la lista.")
                    continue

                if availableDays[daySelection] != 'Disponible':
                    print("El día ya está ocupado por", availableDays[daySelection])
                else:
                    availableDays[daySelection] = input("Ingrese el nombre del cliente a reservar: ")
                    print("Reserva realizada a nombre de", availableDays[daySelection])

            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            again = input('Marque (s) para realizar otra reserva y (n) para continuar\n') 
            if again.lower() == 's':
                continue
            else:
                break
        
        #Seleccion de sedes para reservar:
        while verify_order0:
            for x in campusList:
                print(x)
            try:    
                campusSelection = int(input('Ingrese el numero de la sede para reservar: ')) - 1
                if campusSelection < 0 or campusSelection >= len(availableTables):
                    print("Selección inválida. Por favor, elija un número de la lista.")
                    continue 

                if availableCampus[campusSelection] != 'Disponible':
                    print("La sede ya está ocupado por", availableCampus[campusSelection])
                else:
                    availableCampus[campusSelection] = input("Ingrese el nombre del cliente a reservar: ")
                    print("Reserva realizada a nombre de", availableCampus[campusSelection])

            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            again = input('Marque (s) para realizar otra reserva y (n) para continuar\n')
            if again.lower() == 's':
                continue
            else: 
                break 

        #Seleccion de mesas para reservar:
        while verify_order0:
            try:    
                tableSelection = int(input('Ingrese el numero de mesa para reservar: ')) - 1
                peopleSelection = int(input('Ingrese el numero de personas por mesa: ')) 
                if tableSelection < 0 or tableSelection >= len(availableTables):
                    print("Selección inválida. Por favor, elija un número de la lista.")
                    continue

                if availableTables[tableSelection] != 'Disponible':
                    print("La mesa ya está ocupada por", availableTables[tableSelection])
                else:
                    availableTables[tableSelection] = input("Ingrese el nombre del cliente a reservar: ")
                    print("Reserva realizada a nombre de", availableTables[tableSelection], '\n Para un total de:',peopleSelection)

            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            again = input('Marque (s) para realizar otra reserva y (n) para finalizar\n')
            if again.lower() == 's':
                continue
            else:
                break 

    availability()
    
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
        
        file=open("pedidos.txt","a")
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
        file.write("Numero de mesa: "+str(table_selection)+"\n"+"Plato ordenado: "+str(dish)+'\n'+"cantidad: "+str(amount_dish)+"\n"+
                               "bebida ordenada: "+str(drink)+'\n'+"cantidad: "+str(amount_drinks)+"\n"+"Postre ordenado: "+str(dessert)+'\n'+"cantidad: "+str(amount_dessert)+"\n")
        file.close()
                    
        

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

        elif select_option == 3:
            print("Salir")
            break

        else:
            print("Opcion invalida")

def option6():
    print("\nUsted selecciono la opcion:\n6.Facturacion")    
    print('***Pedidos ingresados***')
    file=open("pedidos.txt","r")
    information=file.read()
    information_inTxt = information.split("\n")
    print(information_inTxt)
    file.close()
    repeat=True
    while repeat:    
        file=open("recibo.txt","a")
        name=str(input("Ingrese el nombre del cliente: "))
        way_To_Pay2 = str(input('Ingrese el metodo de pago: '))
        date=str(input("Ingrese la fecha: "))
        dish=str(input("Ingrese el plato ordenado: "))
        dessert=str(input("Ingrese el postre ordenado: "))
        drink=str(input("Ingrese la bebida ordenado: "))
        amount_dish = int(input("Ingrese la cantidad de " + dish ))
        amount_drinks = int(input("Ingrese la cantidad de " + drink ))
        amount_dessert = int(input("Ingrese la cantidad de " + dessert ))
        dish_price=4500
        dessert_price=2000
        drink_price=1200
        rawPrice_dish=dish_price*amount_dish
        rawPrice_drinks=drink_price*amount_drinks
        rawPrice_dessert=dessert_price*amount_dessert
        raw_price=rawPrice_drinks+rawPrice_dish+rawPrice_dessert
        iva=raw_price*0.13
        tax_service=raw_price*0.10
        total=raw_price+iva+tax_service
            
            
        file.write("**Restaurante sabores Deliciosos**"+"\n"+"fecha: "+str(date)+"\n"+"nombre cliente: "+str(name)+"\n"+
                       "Plato ordenado: "+str(dish)+'\n'+"cantidad: "+str(amount_dish)+" "+str(rawPrice_dish)+"\n"+
                        "bebida ordenada: "+str(drink)+'\n'+"cantidad: "+str(amount_drinks)+" "+str(rawPrice_drinks)+"\n"+"Postre ordenado: "+str(dessert)+'\n'+"cantidad: "+
                        str(amount_dessert)+" "+str(rawPrice_dessert)+"\n"+"Precio bruto: "+str(raw_price)+"\n"+"IVA: 13%"+"\n"+"Impuesto de Venta: 10%"+"\n"+
                        str(total)+"\n"+'Metodo de pago: '+str(way_To_Pay2)+'\n'"¡Gracias por su visita vuelva pronto!"+"\n\n")
        file.close()
        generate=input("Desea generar la factura? (si/no) ")
        if generate=="si":
            repeat=False
    


while login.lower() == "si":
    principal_menu()
    option = int(input("Seleccione una opción: "))

    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        try: 
            option3(availabilityList, group)
        except NameError:
            print('¡No se ha registrado ningun cliente aun!')    
    elif option == 4:
        option4()
    elif option == 5:
        option5()
    elif option == 6:
        try:
            option6()
        except FileNotFoundError:
            print('¡Se requiere ingresar los datos anteriores para poder almacenar pedidos!')
    elif option == 7:
        print("\nUsted selecciono la opcion:\n7.Salir")
        break
    else:
        print("Ingrese una opcion valida\n")
        continue
        print("Ingrese una opcion valida\n")
        continue
        
  
