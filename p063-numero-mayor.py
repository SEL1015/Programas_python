#p063-numero-mayor


while True:
        print("\n--- Buscando el número más grande ---")
        print("Introduce números (ingresa 0 para finalizar la serie):")
        
        # Inicializamos el máximo como None para saber que aún no hay números
        maximo = None
        
        while True:
            try:
                numero = float(input(" -> Ingresa un número: "))
                
                if numero == 0:
                    break  # Detiene la entrada de datos
                
                # Lógica para encontrar el mayor
                if maximo is None or numero > maximo:
                    maximo = numero
                    
            except ValueError:
                print("Error: Por favor, ingresa un número válido.")

        # Mostrar el resultado de la serie
        if maximo is not None:
            print(f"\nEl número más grande introducido fue: {maximo}")
        else:
            print("\nNo se introdujeron números válidos en esta serie.")

        # Preguntar si desea repetir el programa
        continuar = input("\n¿Desea analizar otra serie (S/N)? ").upper()
        if continuar != 'S':
            print("Programa finalizado.")
            break

