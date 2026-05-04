"""Escribe un programa que procese una lista de números. Debes implementar lo siguiente:
1. Una función que lea y devuelva una lista de números enteros (puedes reusar la hecha en clase).
2. Una función que reciba un número entero y devuelva la suma de sus dígitos individuales (ej: 1971 ->
1+9+7+1 = 18).
3. Una función principal que reciba la lista de números. Esta debe usar la función anterior para crear y
devolver una nueva lista que contenga la suma de los dígitos de cada número original.
El programa debe imprimir la lista original y la nueva lista con las sumas.
Ejemplo de Ejecución:
Dame los números (separados por espacio): 1971 2345 2015 2022
La lista de números original : [1971, 2345, 2015, 2022]
La lista con las suma de dígitos de los números: [18, 14, 8, 6]"""
print('\033[H\033[J')
from typing import List 
def leer_numeros() -> List[int]:
    numeros_str = input("Dame los números (separados por espacio): ")
    numeros = [int(num) for num in numeros_str.split()]
    return numeros
def suma_digitos(numero: int) -> int:
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

def procesar_numeros(numeros: List[int]) -> List[int]:
    suma_digitos_lista = []
    for numero in numeros:
        suma_digitos_lista.append(suma_digitos(numero))
    return suma_digitos_lista


def main():
    numeros = leer_numeros()
    suma_digitos_lista = procesar_numeros(numeros)
    
    print(f"La lista de números original : {numeros}")
    print(f"La lista con las suma de dígitos de los números: {suma_digitos_lista}")
if __name__ == "__main__":
    main()
    print('\033[H\033[J')

