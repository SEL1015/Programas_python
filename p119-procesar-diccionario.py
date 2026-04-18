#p119-procesar-diccionario.py
""" Define dos listas:
o nom = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
o suld = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]
• Crea un diccionario nomina combinando ambas listas (los nombres son las llaves, los sueldos son los valores).
• Muestra el diccionario nomina resultante.
• Itera sobre el diccionario y muestra su contenido de cuatro formas:
o Mostrando solo las llaves (usando keys()).
o Mostrando solo los valores (usando values()).
o Iterando por las llaves y accediendo al valor (ej. for llave in dic: ...).
o Mostrando la llave y el valor simultáneamente (usando items()).
• Calcula y muestra la suma total de los suld.
• Calcula y muestra el promedio de los suld."""
print('\033[H\033[J')


# Crear listas
nom = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
suld = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

# Crear diccionario combinando listas
nomina = dict(zip(nom, suld))

# Mostrar diccionario
print("Diccionario de nómina:")
print(nomina)

# Iterar llaves
print("\n--- Iterando Llaves (keys) ---")
for nombre in nomina.keys():
    print(nombre)

# Iterar valores
print("\n--- Iterando Valores (values) ---")
for sueldo in nomina.values():
    print(sueldo)

# Iterar llaves accediendo a valores
print("\n--- Iterando Llave y Valor (accediendo por llave) ---")
for nombre in nomina:
    print(nombre, "->", nomina[nombre])

# Iterar con items
print("\n--- Iterando Llave y Valor (items) ---")
for elemento in nomina.items():
    print(elemento)

# Cálculos
suma = sum(nomina.values())
promedio = suma / len(nomina)

print("\n--- Cálculos ---")
print("Suma total de suld:", suma)
print("Promedio de suld:", round(promedio, 2))