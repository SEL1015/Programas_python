#p125-segundo-sxamen-parcial.py
print('\033[H\033[J') 
"""1. 💻 PLANTEAMIENTO DEL PROBLEMA
Se desea procesar el registro de vuelos de una aerolínea ("AeroRegistro"). Para ello, deberá solicitar al
usuario los siguientes datos por cada vuelo:
• num_vuelo (identificador del vuelo, ej. 'AA-101')
• origen (ciudad de salida, ej. 'Ciudad de México')
• destino (ciudad de llegada, ej. 'Guadalajara')
• aerolinea (nombre de la aerolínea, ej. 'AeroMéxico', 'Volaris', 'Interjet')
• pasajeros (número de pasajeros a bordo, ej. 180)
• tarifa (precio del boleto en pesos, ej. 2350.75)
Los datos se deben almacenar en una lista, donde cada elemento de la lista sea un diccionario con los
datos de un vuelo.
Nota: No olvides documentar las partes importantes del código, explicando qué hace ese fragmento en
específico. listo 
2. 📊 REQUISITOS DE SALIDA
Al terminar la captura (ej. cuando el usuario ingrese un número de vuelo vacío), el programa deberá
procesar la lista e imprimir:
• Datos Crudos: La lista de diccionarios tal como se almacenó.
• Formato Tabular: Los datos de los vuelos organizados en una tabla clara.
Resumen del Registro:
• Total de vuelos registrados.*
• Cuántos vuelos por aerolínea.*
• Cuántos vuelos por ciudad de destino. *
• La suma total de pasajeros y el promedio de pasajeros por vuelo.
• La suma total de tarifas (considerando una sola tarifa por vuelo) y la tarifa promedio.
• El número de vuelo y la tarifa del vuelo más caro y del más barato."""

#Funcion 1 cpaturar los datos del vuelo 

titulo = " 🛩️🛩️🛩️🛩️  Aero Registro - Sistema de Vuelos  🛩️🛩️🛩️"
ancho = 60
barra = titulo.center(ancho)

print("\033[44m\033[37m" + barra + "\033[0m")  # fondo azul, texto blanco # Cambio de texto formato para el titulo

#COMIENZO DE PROCESOS DE PROGRAMACION 
vuelos=[] # Almacena los datos de los vuelos 
while True:
    num_vuelo = input("Ingrese el número de vuelo (o deje vacío para terminar): ")
    if not num_vuelo:  # Si el usuario ingresa una cadena vacía, se termina la captura
        break
    origen = input("Ingrese la ciudad de origen: ")
    destino = input("Ingrese la ciudad de destino: ")
    aerolinea = input("Ingrese el nombre de la aerolínea: ")
    pasajeros = int(input("Ingrese el número de pasajeros a bordo: "))
    tarifa = float(input("Ingrese el precio del boleto en pesos: "))

    # Crear un diccionario con los datos del vuelo y agregarlo a la lista
    vuelo = {
        "num_vuelo": num_vuelo,
        "origen": origen,
        "destino": destino,
        "aerolinea": aerolinea,
        "pasajeros": pasajeros,
        "tarifa": tarifa
    }
    vuelos.append(vuelo)

    #Funcion 2 Requcitos de salida 

print("\n--- Datos Crudos ---")

for vuelo_ingresado in vuelos:
    print(vuelo_ingresado)

print("\n--- Forma Tabular  ---")
print(f"{"Numero de vuelo ":<20}{"Origen":<20}{"Destino":<20}{"Aerolinea":<20}{"Pasajeros":<15}{"Tarifa":<10}")
for vuelo in vuelos:
    print(f"{vuelo['num_vuelo']:<20}{vuelo['origen']:<20}{vuelo['destino']:<20}{vuelo['aerolinea']:<20}{vuelo['pasajeros']:<15}{vuelo['tarifa']:<10.2f}")   

    #Funcion 3 Resum del Registro Obtenidos 
total_vuelos=len(vuelos)
vuelos_aerolinea={}
vuelos_dest={}
total_pasajeros=0
total_tarif=0
for vuelo in vuelos:
    aerolinea = vuelo['aerolinea']
    destino = vuelo['destino']
    pasajeros = vuelo['pasajeros']
    tarifa = vuelo['tarifa']

    # Contar vuelos por aerolínea
    if aerolinea in vuelos_aerolinea:
        vuelos_aerolinea[aerolinea] += 1
    else:
        vuelos_aerolinea[aerolinea] = 1

    # Contar vuelos por ciudad de destino
    if destino in vuelos_dest:
        vuelos_dest[destino] += 1
    else:
        vuelos_dest[destino] = 1

    total_pasajeros += pasajeros
    total_tarif += tarifa

    #Calculo de promedios  
promedio_pasajeros = total_pasajeros / total_vuelos if total_vuelos > 0 else 0

# Calculo de La suma total de tarifas (considerando una sola tarifa por vuelo) y la tarifa promedio.
promedio_tarifa = total_tarif / total_vuelos if total_vuelos > 0 else 0

#Calculo de vuelo mas caro y mas barato 
print("\n--- Vuelo más caro y más barato ---")

if len(vuelos) > 0:
    # Tomamos el primer vuelo como referencia
    vuelo_caro = vuelos[0]
    vuelo_barato = vuelos[0]

    # Recorremos la lista
    for v in vuelos:
        if v["tarifa"] > vuelo_caro["tarifa"]:
            vuelo_caro = v
        
        if v["tarifa"] < vuelo_barato["tarifa"]:
            vuelo_barato = v

    # Mostrar resultados
    print(f"Vuelo más caro: {vuelo_caro['num_vuelo']} - Tarifa: ${vuelo_caro['tarifa']:.2f}")
    print(f"Vuelo más barato: {vuelo_barato['num_vuelo']} - Tarifa: ${vuelo_barato['tarifa']:.2f}")

else:
    print("No hay vuelos registrados")


print("\n--- Resumen del Registro ---")
print(f"Total de vuelos registrados: {total_vuelos}")   
print("\nVuelos por aerolínea:")
for aerolinea, count in vuelos_aerolinea.items():
    print(f"{aerolinea}: {count} vuelos")
print("\nVuelos por ciudad de destino:")
for destino, count in vuelos_dest.items():
    print(f"{destino}: {count} vuelos")
print(f"\nTotal de pasajeros: {total_pasajeros}")
print(f"Promedio de pasajeros por vuelo: {promedio_pasajeros:.2f}")
print(f"Total de tarifas: {total_tarif:.2f}")
print(f"Promedio de tarifa por vuelo: {promedio_tarifa:.2f}")


print("\ ♥️🛩️🛩️🛩️nGRACIAS POR PARTICIPAR🛩️🛩️🛩️♥️")

