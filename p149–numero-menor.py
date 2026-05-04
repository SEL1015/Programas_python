# p149-numero-menor.py
"""Crea un programa que incluya una función. Dicha función debe solicitar 3 números enteros al usuario y devolver el
menor.
Ejemplo de Ejecución:
Introduce el primer número: 15
Introduce el segundo número: 8
Introduce el tercer número: 22
El número menor es: 8"""
   
def obtener_menor():
    print('\033[H\033[J')
    # Solicitar los 3 números enteros al usuario
    num1 = int(input("Introduce el primer número: ")) ## aqui pide al usuario el primer numero 
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))
    
    # Lógica para encontrar el menor
    menor = min(num1, num2, num3)
    
    return menor

# Llamada a la función e impresión del resultado
resultado = obtener_menor()
print(f"El número menor es: {resultado}")

