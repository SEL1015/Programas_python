"""Desarrolla un programa que funcione como un conversor de unidades de longitud. El programa debe mostrar un
menú y utilizar dos funciones separadas:
1. Una función para convertir pulgadas a centímetros (fórmula: $cm = pulgadas \times 2.54$).
2. Una función para convertir metros a pies (fórmula: $pies = metros \times 3.281$).
El programa debe solicitar los datos al usuario según la opción elegida y mostrar el resultado.
Ejemplo de Ejecución:
*** Conversor de Unidades ***
1. Pulgadas a Centímetros
2. Metros a Pies
3. Salir
Elige una opción: 1
Introduce la cantidad en pulgadas: 10
10.0 pulgadas equivalen a 25.4 centímetros."""
print('\033[H\033[J')
def pulgadas_a_centimetros(pulgadas: float) -> float:
    return pulgadas * 2.54
def metros_a_pies(metros: float) -> float:
    return metros * 3.281   
def mostrar_menu():
    print("*** Conversor de Unidades ***")
    print("1. Pulgadas a Centímetros")
    print("2. Metros a Pies")
    print("3. Salir")   
def main():

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == '1':
            pulgadas = float(input("Introduce la cantidad en pulgadas: "))
            centimetros = pulgadas_a_centimetros(pulgadas)
            print(f"{pulgadas} pulgadas equivalen a {centimetros} centímetros.")
        elif opcion == '2':
            metros = float(input("Introduce la cantidad en metros: "))
            pies = metros_a_pies(metros)
            print(f"{metros} metros equivalen a {pies} pies.")
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 3.")
if __name__ == "__main__":
    main()



