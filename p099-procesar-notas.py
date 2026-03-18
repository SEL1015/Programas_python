# p099-procesar-notas.py
"""
Leer un número indeterminado de notas (notas) entre 0 y 100, deteniéndose cuando el usuario introduzca
un 0. Validar que todas las notas introducidas estén dentro del rango [0,100].
"""
print('\033[H\033[J')
print('Procesador notas entre 0 y 100  \n')
print("usa --0--  para terminar):\n")
notas = []
suma = 0.0
while True:
    try:
        n = float(input("Calificación > "))
        if n == 0: break
        if 0 <= n <= 100:
            notas.append(n)
            suma += n
        else:
            print("Error: la calificación debe estar entre 0 y 100.")

    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")
# Verificar si se ingresaron datos
if len(notas) == 0:
    print("No se ingresaron notas.")
else:
    # Cálculos
    cantidad = len(notas)
    suma = sum(notas)
    promedio = suma / cantidad
    maxima = max(notas)
    minima = min(notas)

    # Notas menores al promedio
    menores = [nota for nota in notas if nota < promedio]

    # Resultados
    print("\n---📊 RESULTADOS----")
    print("Cantidad de notas:", cantidad)
    print("Lista de notas:", notas)
    print("Suma:", suma)
    print("Promedio:", promedio)
    print("Nota máxima:", maxima)
    print("Nota mínima:", minima)
    print("Cantidad menores al promedio:", len(menores))
    print("Notas menores al promedio:", menores)

print("♥️♥️♥️GRACIAS POR PARTICIPAR♥️♥️♥️")