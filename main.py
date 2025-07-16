from funciones import *


#MENU PRINCIPAL
while True:
    print("***MENU PRINCIPAL***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Listado de productos.")
    print("4. Salir.")

    op = input("Ingrese opción: ")
    if op == "1":
        stock_marca()
    elif op == "2":
        busqueda_por_precio()
    elif op == "3":
        ordenar_productos()
    elif op == "4":
        print("Programa finalizado.")
        break
    else:
        print("Debe seleccionar una opción válida!!")