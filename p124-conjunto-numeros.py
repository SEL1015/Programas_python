#p124-conjunto-numeros.py
"""Dadas las siguientes tres listas de números:
• Lista 1: 50, 60, 70, 80, 90, 100, 200
• Lista 2: 60, 90, 100, 300, 400, 500
• Lista 3: 10, 20, 60, 90, 70, 100, 600, 700
Instrucciones:
1. Crear y mostrar los conjuntos A, B y C a partir de las listas.
2. Calcular y mostrar los resultados de las siguientes operaciones:
o Unión (A | B)
o Unión (B | C)
o Diferencia (A - C)
o Diferencia Simétrica (B ^ C)
o Intersección (B & C)
3. Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes preguntas:
o ¿Es A subconjunto de B?
o ¿Es C subconjunto de A?
o ¿Está el número 100 en A?
o ¿Está el número 60 en A, B y C?
o ¿No está el número 900 en C?"""


print('\033[H\033[J')
L1 = ["50", "60", "70", "80", "90" ,"100", "200"]
L2 = ["60", "90", "100", "300", "400","500"]
L3 = ["10", "20", "60", "90", "70", "100", "600", "700"]

# Crear conjuntos a partir de las listas 
A = set(L1)
B = set( L2)
C= set (L3)

print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto B:", C)

#Operaciones con conjuntos resultados 
print("\n--- OPERACIONES DE CONJUNTOS  ---")
print("Unión (A | B):", A | B)
print("Unión (B | C):", B | C)
print("Diferencia (A - B):", A - B)
print("Diferencia simétrica (B ^ C):", B ^ C)
print("Intersección (B & C):", B & C)



# Verificaciones VERDADERO /FALSO DE CONJUNTOS 
print("\n--- Verificaciones ---")
# Subconjunto A SUBCONJUNTO DE B
print("¿ES A subconjunto de B?:",
      {"A"}.issubset(B))
# Subconjunto C SUBCONJUNTO DE A
print("¿ES C subconjunto de A?:",
      {"C"}.issubset(A))


# Pertenencia del numero 100 en A 
#¿Está el número 100 en A?
print("¿Está el número 100 en A?:", "100" in A)


#¿Está el número 60 en A, B y C?
print("¿Esta el numero 60 en A,B,Y C?:","60" in A and "60" in B and "60" in C)

# No pertenencia
print("¿'El numero 900' NO está en B?:", "900" not in B)


print("\nGRACIAS POR PARTICIPAR")