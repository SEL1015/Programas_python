#p042-precio-entrada-cine#
# Problema: Crea un programa para la taquilla de un cine que determine el precio de una entrada según la edad del cliente. El programa debe solicitar la edad y mostrar el precio correspondiente, siguiendo estas reglas:
# Menores de 5 años: Entran gratis.//
# Niños (5 a 12 años): Pagan $5.//
# Adultos (13 a 64 años): Pagan $10.
# Tercera edad (65 años o más): Pagan $7.
# Ejemplos de ejecución:
#Entrada: Edad: 4
# Salida: Tu entrada es gratis.
# Entrada: Edad: 10
# Salida: El precio de tu entrada es de $5.
# Entrada: Edad: 35
#Salida: El precio de tu entrada es de $10.3

print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]") 

#Entrada de datos
print("Determinar el precio de la entrada segun la edad del cliente ")
print("Bienvenido a esta aventura cinematografica  ")

#Declaracion de variables

nombre= input("Dame tu nombre ")
edad=int(input("Ingresa tu edad : "))#Input por ingreso de valores enteros 

#Evaluar con sentencias if/elif
if edad <=1 or edad <=5:
    print(f"Hola, {nombre} 👶 eres menor,  tu entrada es GRATIS ")

elif edad >= 6 and edad <12:
    print(f"Hola, {nombre}  👦eres niño , tu entrada tiene un costo de : $ 5 ")   

elif edad >= 13 and edad <64:
    print(f"Hola, {nombre}  🧑eres un adulto , tu entrada tiene un costo de : $ 10 ")   

elif edad >=65 and edad <=75:
    print(f"Hola, {nombre}  👵eres de la tercera edad  , tu entrada tiene un costo de : $ 7 ")   
else:
    print("Error EDAD INVADLIDA")

print("   ------Bienvenidos -----")
print("🍿🍿🍿🍿🍿Fin del tiket de cine 🎞️🍿🍿🍿🍿🍿🍿")