"""Desarrolla un programa que calcule el factorial de cada número en una lista. Debes implementar:
1. Una función que lea y devuelva una lista de números enteros.
2. Una función que reciba un número entero y devuelva su factorial (ej: 5 -> 120).
3. Una función principal que reciba la lista de números. Esta debe usar la función factorial para crear y
devolver una nueva lista con los factoriales de cada número.
El programa debe imprimir la lista original y la lista de factoriales."""
print('\033[H\033[J')
from typing import List 
def leer_numeros() -> List[int]:
    numeros_str = input("Dame los números (separados por espacio): ")
    numeros = [int(num) for num in numeros_str.split()]
    return numeros
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def procesar_numeros(numeros: List[int]) -> List[int]:
    factoriales = []
    for numero in numeros:
        factoriales.append(factorial(numero))
    return factoriales
def main():
    numeros = leer_numeros()
    factoriales = procesar_numeros(numeros)
    
    print(f"La lista de números original : {numeros}")
    print(f"La lista con los factoriales de los números: {factoriales}")