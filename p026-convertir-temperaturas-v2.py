# p026–convertir-temperaturas-v2.py
# Convierte Celcius a Fahrenheit y viseversa


print("\033[2J\033[H") # Borra la pantalla usando secuencias de escape ANSI
print("* ConvierteConversion de temperaturas  entre Celsius y Fahrenheit *\n")

print("[1] para convertir frenheit a centrigados ")
print("[2] para convertir a Centrigrados a farenheit")

opcion = input("Elige una opción? ").upper()

# Validación de la opción
if opcion == "1":
    print("\n Convirtiendo a Celsius...")
    f = float(input("Introduce los grados Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"\n Resultado: {f:.2f}°F equivalen a {c:.2f}°C.")

elif opcion == "2":
    print("\n Convirtiendo a Fahrenheit...")
    c = float(input("Introduce los grados Celsius: "))
    f = (c * 9 / 5) + 32
    print(f"\n Resultado: {c:.2f}°C equivalen a {f:.2f}°F.")

else:
    print(f"\n Opción '{opcion}' no válida. Por favor, reinicia el programa y elige solo '1' o '2'.")

print("\n* ¡Programa finalizado! *")