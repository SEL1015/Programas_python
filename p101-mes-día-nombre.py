# p101-mes-día-nombre.py
"""
Leer un número de mes (ej. 4). Guardar los días de cada mes en una lista y los nombres de los meses en otra
lista. Asumir 28 días para febrero. Imprimir el nombre del mes y la cantidad de días del mes correspondiente (ej.
marzo, 30).
"""
print('\033[H\033[J')

#DECLARACION DE VARIABLES 

meses = [" 🥏Enero", " ♥️Febrero♥️♥️", "🌻Marzo", "👦Abril", "👩Mayo", "👨Junio",
         "👨‍🎓Julio", "🎈Agosto", "Septiembre", "Octubre", " 🎃Noviembre", "🎅Diciembre"]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

nu_mes = int(input("Introduzca un número de mes (1-12): "))

if 1 <= nu_mes <= 12:
    print("--- Resultados ---")
    print("Mes:", meses[nu_mes - 1])
    print("Días:", dias[nu_mes - 1])
else:
    print("Error: el número de mes debe estar entre 1 y 12.")