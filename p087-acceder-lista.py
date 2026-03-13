
# p087-acceder-lista.py
# Acceder a elementos de una lista
meds = [10, 20, 30, 40, 60, 70, 10, 20, 99]
print("\033[H\033[J")
print("Acceder a los elementos de una lista\n")
print("\nLongitud y contenido de las mediciones :")
print(f"Cuantas mediciones son : {len(meds)}")
print(f"Todas las mediciones : {meds} ")

print("\n Acceder Por indice positivo : ")
print(f"Primera y última medicion  : {meds[0]}, {meds[8]}")

print("\nPor indice negativo : ")
print(f"Primera y última : {meds[-9]}, {meds[-1]}")

print("\n Acceder un rango de valores de la lista  : ")
print(f"De la 2 ala 6 (pos 6 no incluida): {meds[2:6]}")

print("\nPor saltos :")
print(f"Las primeras 3 desde el principio : {meds[:3]}")
print(f"Las últimas 3 desde el 6 hasta el final : {meds[6:]}")

#notas
#LEN - LONGITUD DE LISTAS 
#sift-felecha abajo 
#Al colocar : es que incia desde el principio
# al final : es que incia del 3 al final 