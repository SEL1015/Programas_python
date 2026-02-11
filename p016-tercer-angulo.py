#p016-tercer-angulo
#Calcular el tercer angulo de un triangulo

print("\033[h\033[j")#imprime una secuencia ansi que borra la pantalla]]")
print("Calcular el tercer angulo de un triangulo")
#Entrada de datos 
angulo1 =int(input("Ingrese el primer angulo del triangulo:"))
angulo2 =int(input("Ingrese el segundo angulo del triangulo:"))
angulo3 = 180 - (angulo1 + angulo2) 

#Salida 
print(f"El tercer angulo del triangulo es : {angulo3:.2f}")
