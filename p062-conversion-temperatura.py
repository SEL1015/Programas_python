#p062-conversion-temperatura


while True:
        try:
            # 1. Entrada de datos
            inicio = int(input("Introduce la temperatura inicial (°C): "))
            final = int(input("Introduce la temperatura final (°C): "))
            # Validar si el rango es ascendente
            if inicio > final:
                print("La temperatura inicial debe ser menor o igual a la final.")
                continue

            print(f"\n{'Celsius (°C)':<15} | {'Fahrenheit (°F)':<15}")
            print("-" * 35)

            # 2. Bucle while para recorrer el rango
            temp_actual = inicio
            while temp_actual <= final:
                # Fórmula de conversión
                fahrenheit = (temp_actual * 1.8) + 32
                
                print(f"{temp_actual:<15} | {fahrenheit:<15.2f}")
                
                temp_actual += 1 # Incremento de uno en uno

        except ValueError:
            print("Error: Por favor, introduce números enteros válidos.")
            continue

        # 3. Opción de continuar
        opcion = input("\n¿Desea realizar otra conversión (S/N)? ").upper()
        if opcion != 'S':
            print("Programa finalizado.")
            break

