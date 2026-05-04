"""Crea un programa que calcule estadísticas básicas (poblacionales) para una lista de números. El programa debe
incluir:
1. Una función para leer una lista de números enteros.
2. Funciones separadas para calcular y devolver cada una de las siguientes estadísticas:
o Número mayor
o Número menor
o Media (promedio)
o Varianza poblacional
o Desviación estándar poblacional

El programa principal debe leer la lista e imprimir todos los resultados estadísticos de forma clara.
Ejemplo de Ejecución:
Dame números (separados por espacio): 5 6 6 7 8 9 10 10
Lista de números: [5, 6, 6, 7, 8, 9, 10, 10]
Estadísticas:
Media : 7.625
Mayor : 10
Menor : 5
Varianza : 3.234
Desviación estándar: 1.798
Dame números: 5 6 6 7 8 9 10 10
Lista de números: [5, 6, 6, 7, 8, 9, 10, 10]
La media: 7.625
Mayor de los datos: 10
Menor de los datos: 5
Varianza: 3.234
Desviación estándar: 1.798"""
print('\033[H\033[J')
from typing import List
print('Dame números (separados por espacio): ', end='')
numeros: List[int] = list(map(int, input().split()))                    
print(f'Lista de números: {numeros}')
def media(nums: List[int]) -> float:
    return sum(nums) / len(nums)
def mayor(nums: List[int]) -> int:
    return max(nums)
def menor(nums: List[int]) -> int:

    return min(nums)
def varianza(nums: List[int]) -> float:
    m: float = media(nums)
    return sum((x - m) ** 2 for x in nums) / len(nums)
def desviacion_estandar(nums: List[int]) -> float:
    return varianza(nums) ** 0.5
print('Estadísticas:')
print(f'Media : {media(numeros):.3f}')
print(f'Mayor : {mayor(numeros)}')

print(f'Menor : {menor(numeros)}')
print(f'Varianza : {varianza(numeros):.3f}')
print(f'Desviación estándar: {desviacion_estandar(numeros):.3f}')

