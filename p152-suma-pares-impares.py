"""Crea un programa que sume números pares o impares dentro de un rango especificado. El programa debe tener
una función que reciba tres parámetros: un número de inicio, un número de fin y una letra ('P' o 'I').
• Si la letra es 'P', la función debe devolver la suma de todos los números pares en ese rango (incluyendo
los límites).
• Si la letra es 'I', la función debe devolver la suma de todos los números impares en el rango.
El programa principal debe mostrar un menú, pedir los datos al usuario y mostrar el resultado de la suma.
Ejemplo de Ejecución:
*** Suma en Rango ***
Introduce el número inicial: 5
Introduce el número final: 15
¿Qué deseas sumar? (P)ares o (I)mpares: P
La suma de los números pares entre 5 y 15 es: 50
(Cálculo: 6 + 8 + 10 + 12 + 14 = 50)"""
print('\033[H\033[J')
def suma_p_inpares(inicio: int, fin: int, tipo: str) -> int:
    suma = 0
    for numero in range(inicio, fin + 1):
        if tipo.upper() == 'P' and numero % 2 == 0:
            suma += numero
        elif tipo.upper() == 'I' and numero % 2 != 0:
            suma += numero
    return suma
def main():     
    print("*** Suma en Rango ***")
    inicio = int(input("Introduce el número inicial: "))
    fin = int(input("Introduce el número final: "))
    tipo = input("¿Qué deseas sumar? (P)ares o (I)mpares: ")
    
    resultado = suma_p_inpares(inicio, fin, tipo)
    
    if tipo.upper() == 'P':
        print(f"La suma de los números pares entre {inicio} y {fin} es: {resultado}")
    elif tipo.upper() == 'I':
        print(f"La suma de los números impares entre {inicio} y {fin} es: {resultado}")
    else:
        print("Opción no válida. Por favor, elige 'P' para pares o 'I' para impares.")  
if __name__ == "__main__":
    main()

