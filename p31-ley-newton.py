# p31-2da-ley-de-newton.py
# Calcular fuerza, masa o aceleración según la elección del usuario.

#impresion del menu de opciones 
print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]")
print("--- Calculadora de la 2da Ley de NEWTON ---")
print("[F] Calcular la Fuerza      (fuerza = masa * aceleración)")#Se muestra la formula
print("[M] Calcular la Masa        (masa = fuerza / aceleración)")
print("[A] Calcular la Aceleración (aceleración = fuerza / masa)")
opcion = input("Opcion? ").upper() # mayusculas

# La estructura if/elif/else ejecuta el cálculo correcto
if opcion == "F":
    print("\n Calculando la Fuerza...")
    masa = float(input("Dame la masa: "))
    aceleracion = float(input("Dame la aceleración: "))
    fuerza = masa * aceleracion
    print(f" La fuerza es: {fuerza:,.2f} ")

elif opcion == "M":
    print("\n Calculando la Masa...")
    fuerza = float(input("Dame la fuerza: "))
    aceleracion = float(input("Dame la aceleración: "))
    masa = fuerza / aceleracion
    print(f" La masa es: {masa:,.2f} ")

elif opcion == "A":
    print("\n Calculando la Aceleración...")
    fuerza = float(input("Dame la fuerza: "))
    masa = float(input("Dame la masa: "))
    aceleracion = fuerza / masa
    print(f" La aceleración es: {aceleracion:,.2f} ")
else:
    print("\n Opción inválida. Por favor, elige F,M,A ")

print("Proceso terminado , gracias por visitar este programa ")
