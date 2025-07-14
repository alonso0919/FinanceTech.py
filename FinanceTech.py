#Bienvenida y presentación
print ("FinanceTech")
print ("BIENVENID@ A TU REGISTRO DE INGRESOS")
print ()

#Lista de datos
lista_datos = []

# Captura del nombre
name = input("Escribe tu nombre: ") 
lista_datos.append("Nombre: "+name)

print(f"Hola, {name}! Qué quieres hacer hoy?\n")

# Menú 
accion = ""
while True:
    if not accion:
        print("MENÚ :)")
        print("1.- Captura de mes")
        print("2.- Tipos de ingreso")
        print("3.- Ingresar gastos por categoría")
        print("4.- Calcular ahorros")
        print("5.- Recomendaciones")
        print("6.- Salir y resúmen")
        accion = input("INSERTE NÚMERO: ")
        print()

    match accion:
        case "1":
            mes = input("Escribe el mes a registrar: ") 
            lista_datos.append("Mes: "+mes)
            print("Captura de mes realizada.\n")

        case "2":
            ingreso = input("Tipo de ingreso a registrar: ")
            cantidadin = input("Cantidad: ")
            lista_datos.append("Tipo de ingreso: "+ingreso)
            lista_datos.append("Cantidad: "+cantidadin)
            print("Captura realizada.\n")

        case "3":
            print("Gastos por categoría.\n")
            gasto = input("Tipo de gasto a registrar: ")
            cantidadgas = input("Cantidad: ")
            lista_datos.append("Tipo de gasto: "+gasto)
            lista_datos.append("Cantidad: "+cantidadgas)
            print("Captura realizada.\n")

        case "4": 
            print("Cálculo de ahorros.\n")
            print("Tus ingresos: "+cantidadin)
            print("Tus gastos: "+cantidadgas)
            ahorro = float(cantidadin) - float(cantidadgas)
            print("Ahorro total: "+str(ahorro))

        case "5":
            print("RECOMENDACIÓN: ")
            print("1.- No gaste en algo si no tiene el doble de esa cantidad.")
            print("2.- No coma sushi tan seguido :)")
        case "6":
            print("Aquí está tu resúmen de lo realizado...")
            print(lista_datos)
            print(f"Hasta luego, {name}!")
            break
        case _:
            print("Opción inválida.\n")

    # Preguntar si quiere hacer otra acción
    accion = input("¿Deseas hacer otra acción? (1/2/3/4/5/6): ")
    print()
          