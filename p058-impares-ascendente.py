##Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el usuario.
##Ejemplo de ejecución:
##Introduce un número límite: 9
##Números impares: 1, 3, 5, 7, 9
##La suma de los impares es: 25
##¿Desea continuar (S/N)? N
#p058-impares-ascendente.py



while True:
        print("PROGRAMA PARA IMPRIMIR NUMEROS IMPARES DE MANERA DESCENDENTE Y SUMAR EL TOTAL DEL RANGO ")
        print('\033[H\033[J')
        #Datos 
        n = int(input("Introduce un número límite: "))
        
        i = 1          # Contador que inicia en el primer impar
        suma = 0       # Acumulador para la suma
        impares = []   # Lista para guardar los números y mostrarlos al final
        
        # Ciclo while para encontrar impares y sumarlos
        while i <= n:
            impares.append(str(i)) # Guardamos el número como texto
            suma += i              # Lo sumamos al total
            i += 2                 # Saltamos al siguiente impar (+2)
        
        #Mostrar resultados
        print(f"Números impares: {', '.join(impares)}")
        print(f"La suma de los impares es: {suma}")
        
        # Preguntar si desea continuar
        if  input('\n¿Deseas realizar otro cálculo (S/N)? ').upper() == 'N':break
print("\nFin del programa")