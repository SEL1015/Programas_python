#p064-verificar-palindromo
#Introduce un número para verificar si es palíndromo: 121
#El número 121 es un palíndromo.
#¿Desea continuar (S/N)? S
#Introduce un número para verificar si es palíndromo: 123
#El número 123 no es un palíndromo.
#¿Desea continuar (S/N)? N

continuar = "S"
while continuar == "S":
    print("\n--- Verificador de Números Palíndromos ---")
    
    try:
        entrada = input("Introduce un número entero: ")
        # Guardamos el original para comparar al final
        numero_original = int(entrada)
        
        # Si el número es negativo, generalmente no se considera palíndromo por el signo
        if numero_original < 0:
            print(f"El número {numero_original} no es palíndromo (los negativos no lo son).")
        else:
            auxiliar = numero_original
            numero_invertido = 0
            
            # Bucle para invertir el número matemáticamente
            while auxiliar > 0:
                # Obtenemos el último dígito con el residuo de 10
                ultimo_digito = auxiliar % 10
                
                # Lo añadimos al número invertido desplazando los anteriores a la izquierda
                numero_invertido = (numero_invertido * 10) + ultimo_digito
                
                # Quitamos el último dígito del auxiliar usando división entera
                auxiliar = auxiliar // 10
            
            # Comparación final
            if numero_original == numero_invertido:
                print(f"¡Sí! El número {numero_original} es palíndromo.")
            else:
                print(f"No, el número {numero_original} no es palíndromo.")

    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")

    # Preguntar si desea continuar
    continuar = input("\n¿Desea verificar otro número (S/N)? ").upper()

print("Gracias ")