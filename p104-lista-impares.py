#p104-lista-impares.py
"""
Leer un entero n. Llenar una lista con los primeros n números impares.
Calcular e imprimir:
• La suma y el promedio de los números.
• Los números que son divisibles entre 3 y su suma.
• Pedir un elemento a buscar en la lista original e indicar si está y en qué posición (índice).
Ejemplo:
Introduzca la cantidad de números impares (n): 6
--- Generación de Lista ---
Lista de los primeros 6 números impares: [1, 3, 5, 7, 9, 11]
--- Cálculos ---
Suma de los números: 36
Promedio de los números: 6.0
--- Divisibles entre 3 ---
Números divisibles entre 3: [3, 9]
Suma de los números divisibles entre 3: 12
--- Búsqueda ---
Introduzca elemento a buscar: 7
Result: El elemento 7 está en la lista en la posición (índice) 3.
"""
print('\033[H\033[J')
# Leer un entero n
n = int(input("Introduzca la cantidad de números impares (n): "))

# Generar la lista de los primeros n números impares
lista_impares = []
num = 1

for i in range(n):
    lista_impares.append(num)
    num += 2

print("--- Generación de Lista ---")
print(f"Lista de los primeros {n} números impares: {lista_impares}")

# Calcular suma y promedio
suma = sum(lista_impares)
promedio = suma / n

print("--- Cálculos ---")
print("Suma de los números:", suma)
print("Promedio de los números:", promedio)

# Encontrar números divisibles entre 3
divisibles_3 = []

for numero in lista_impares:
    if numero % 3 == 0:
        divisibles_3.append(numero)

suma_divisibles = sum(divisibles_3)

print("--- Divisibles entre 3 ---")
print("Números divisibles entre 3:", divisibles_3)
print("Suma de los números divisibles entre 3:", suma_divisibles)

# Buscar un elemento en la lista
buscar = int(input("--- Búsqueda ---\nIntroduzca elemento a buscar: "))

if buscar in lista_impares:
    print(f"Result: El elemento {buscar} está en la lista en la posición (índice) {lista_impares.index(buscar)}.")
else:
    print(f"Result: El elemento {buscar} no está en la lista.")