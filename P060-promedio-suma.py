#p060-promedio-suma.py
#Leer números introducidos por el usuario hasta que ingrese un 0. Al finalizar, mostrar el conteo total de números, la suma y el promedio de la serie.
#Ejemplo de ejecución:
#Introduce números (0 para terminar):
#> 10
#> 5
#> 15
#> 0
#Se introdujeron 3 números.
#La suma es: 30
#El promedio es: 10.0
#¿Desea continuar (S/N)? N

def programa_serie_numerica():
    while True:
        suma = 0
        conteo = 0
        
        print("\n--- Nueva Serie de Números ---")
        print("Introduce números (ingresa 0 para terminar la serie):")
        
        # Bucle para leer números de la serie actual
        while True:
            try:
                numero = float(input(" -> Ingrese un número: "))
                
                if numero == 0:
                    break  # Sale del bucle de lectura
                
                suma += numero
                conteo += 1
                
            except ValueError:
                print("Error: Por favor, introduce un valor numérico válido.")

        # Mostrar resultados de la serie actual
        if conteo > 0:
            promedio = suma / conteo
            print("\n--- Resultados de la Serie ---")
            print(f"Cantidad de números: {conteo}")
            print(f"Suma total: {suma}")
            print(f"Promedio: {promedio:.2f}")
        else:
            print("\nNo se ingresaron números para procesar.")

        # Preguntar si desea iniciar una nueva serie
        continuar = input("\n¿Desea procesar otra serie de números (S/N)? ").upper()
        if continuar != 'S':
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    programa_serie_numerica()