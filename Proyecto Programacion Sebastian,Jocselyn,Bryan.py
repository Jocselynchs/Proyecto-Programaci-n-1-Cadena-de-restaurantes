"""Cadena de restaurantes Sabores Deliciosos"""
""" Primer avance; Generar el primer módulo completo y funcional.
• Generar el segundo módulo completo y funcional.
• Generar el tercer módulo completo y funcional"""

print("Bienvenido a la cadena de restaurantes Sabores Deliciosos")
yes=True
No=False
login=input("¿Desea ingresar al menu?\n Marque Si para ingresar al menu o No para salir del menu")
while login=="si":
    print("Este es su menu")
    print("1.Registrar nueva sede")
    print("2.Modulo de registro de clientes")
    print("3.Modulo e reservaciones del restaurante")
    print("4.Modulo de toma de ordenes y pedidos")
    print("5.Modulo de resgistro de alimentos y bebidas")
    print("6.Modulo de facturacion")
    print("7.Salir.")
    option=int(input("Seleccione una opcion: "))
    if option==1:
        print("Usted selecciono la opcion\n 1.Registrar nueva sede")
    elif option == 2:
        print("Usted selecciono la opcion\n 2.Modulo de registro de clientes")
    elif option == 3:
        print("Usted selecciono la opción\n 3.Modulo e reservaciones del restaurante")
    elif option == 4:
        print("Usted selecciono la opcion\n 4.Modulo de toma de ordenes y pedidos")
    elif option == 5:
        print("Usted selecciono la opcion\n 5.Modulo de resgistro de alimentos y bebidas")
    elif option == 6:
        print("Usted selecciono la opcion\n 6.Modulo de facturacion")
    else:
        print("Usted ha salido del menu")
