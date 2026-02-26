#p061-suma-200-py
#.
#Ejemplo de ejecución:
#Suma actual: 0. Introduce un número: 70
#Suma actual: 70. Introduce un número: 80
#Suma actual: 150. Introduce un número: 55
#Meta de 200 alcanzada.
#Suma final: 205
#Total de números introducidos: 3
#¿Desea continuar (S/N)? NLeer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. Al terminar, mostrar cuántos números se introdujeron y la suma fin
# al

suma_final = 0
conteo_numeros = 0
print('\033[H\033[J')
print("Introduce números para acumular (la meta es 200):")
    
    # El bucle continúa mientras la suma sea menor a 200
while suma_final < 200:
        try:
            numero = float(input(f"Suma actual: {suma_final} | Ingresa un número: "))
            
            suma_final += numero
            conteo_numeros += 1
            
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

    # Resultados finales
print("\n¡Meta alcanzada!")
print(f"Suma final: {suma_final}")
print(f"Cantidad de números introducidos: {conteo_numeros}")

continuar = input("\n¿Desea procesar otra serie de números (S/N)? ").upper()
if continuar != 'S':
        print("Saliendo del programa...")
        break

