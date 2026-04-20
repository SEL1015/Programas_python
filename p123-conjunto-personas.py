#p123-conjunto-personas.py
"""
Dadas las siguientes dos listas de nombres:
• Lista 1: Juan, Maria, Pedro, Jose, Rocio
• Lista 2: Pedro, Juan, Pablo, Mateo, Esther
Instrucciones:
1. Crear y mostrar los conjuntos A (basado en la Lista 1) y B (basado en la Lista 2).
2. Calcular y mostrar los resultados de las siguientes operaciones:
o Unión (A | B)
o Intersección (A & B)
o Diferencia (A - B)
o Diferencia Simétrica (A ^ B)
3. Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes afirmaciones:
o ¿Es {Pablo, Mateo} un subconjunto de B?
o ¿Es A un superconjunto de {Reynaldo, Angelica}?
o ¿Está "Pedro" en el conjunto A?
o ¿No está "Lilia" en el conjunto B?"""

print('\033[H\033[J')
lista1 = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista2 = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

# Crear conjuntos
A = set(lista1)
B = set(lista2)

print("Conjunto A:", A)
print("Conjunto B:", B)

#Operaciones con conjuntos
print("\n--- Operaciones ---")
print("Unión (A | B):", A | B)
print("Intersección (A & B):", A & B)
print("Diferencia (A - B):", A - B)
print("Diferencia simétrica (A ^ B):", A ^ B)

# Verificaciones
print("\n--- Verificaciones ---")

# Subconjunto
print("¿{Pablo, Mateo} es subconjunto de B?:",
      {"Pablo", "Mateo"}.issubset(B))

# Superconjunto
print("¿A es superconjunto de {Reynaldo, Angelica}?:",
      A.issuperset({"Reynaldo", "Angelica"}))

# Pertenencia
print("¿'Pedro' está en A?:", "Pedro" in A)

# No pertenencia
print("¿'Lilia' NO está en B?:", "Lilia" not in B)