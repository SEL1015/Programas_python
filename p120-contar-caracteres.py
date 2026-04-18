#p120-contar-caracteres.py
"""Escribe un programa que pida al usuario que ingrese una CAD de texto.
• Crea un diccionario vacío para almacenar la frecuencia (cantidad de apariciones) de cada carácter.
• Itera sobre cada carácter en la CAD ingresada.
• En cada iteración:
o Si el carácter no existe como llave en el diccionario, agrégalo con un valor de 1.
o Si el carácter ya existe, incrementa su valor actual en 1.
• Al finalizar el ciclo, muestra el diccionario resultante con el conteo de caracteres."""

print('\033[H\033[J')
#INGRES0 DE CAD 
CAD = input("Ingrese una CAD: ")

# Crear diccionario vacío
frecuencia = {}

# Recorrer cada carácter
for caracter in CAD:
    if caracter in frecuencia:
        frecuencia[caracter] += 1
    else:
        frecuencia[caracter] = 1

# Mostrar resultado
print("\nResultado:")
print(frecuencia)