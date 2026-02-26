#Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el usuario.
#Ejemplo de ejecución:
#Introduce un número límite (menor a 100): 92
#Números pares: 100, 98, 96, 94, 92
#La suma de los pares es: 480
#¿Desea continuar (S/N)? N


while True:
        print('\033[H\033[J')
        #Datos 
        n = int(input("Introduce el número límite (menor a 100): "))
        if n > 100:
                print("El número debe ser menor a 100")
                continue
        i = 100        # Iniciamos en el extremo superior
        suma = 0       # Acumulador
        pares = []     # Lista para mostrar los números
            
        # 2. Bucle descendente
        while i >= n:
                # Solo agregamos y sumamos si el número actual es par
                if i % 2 == 0:
                    pares.append(str(i))
                    suma += i
                i -= 1     # Bajamos de uno en uno para no saltar el límite n
        #Mostrar resultados
        print(f"Números pares                   : {', '.join(pares)}")
        print(f"La suma de los numeros pares  es: {suma}")
        if  input('\n¿Deseas realizar otro cálculo (S/N)? ').upper() == 'N':break
print("\nFin del programa")