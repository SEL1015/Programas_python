#p092-lista-de-gastos
#permite llevar el control en una lista de gastos 


gastos= [450.50,120.00,85.90,230.00,55.75]
limite_gasto=100.00


while True:
    print("\n --- Menu de Gestion de Gastos --- ")
    print("1.- Ver todos los  Gastos --- ")
    print("2.- Agregar nuevo  Gasto --- ")
    print("3.- Modificar un gasto existente  --- ")
    print("4.- Eliminar un gasto (por rembolso o error) --- ")
    print("5.- Ver resumen y total de gastos --- ")
    print("6. Salir  --- ")
    opcion= int(input("Elije una opcion (1-6):"))


    if opcion==1:
        print(f"\n Todos los gastos {gastos}")
    elif opcion==2:
        nuevo_gasto=float(input("Nuevo Gasto?"))
        gastos.append(nuevo_gasto)
    elif opcion==3:
        pos=int(input("Posicion del gasto a modificar"))
        gastos[pos]
    elif opcion==4:
        gasto_eliminar=float(input("Gasto a Eliminar"))
        gasto.remove (gasto_eliminar)
    elif opcion==5:
        total_gastado=0
        print("\n Gastos del Mes ")
        for gasto in gastos:
            total_gastado +=gasto
            if gasto>limite_gasto:
                print(f"Gasto excede el Limite {gasto}")
            else:
                print(f"Gasto normal : {gasto}")
        print(f"Total gastado : {total_gastado}")
    elif opcion==6:
        print("\n Gracias por utilizar el sistema")
        break
    else:
        print("\n Opcion NO VALIDA")
