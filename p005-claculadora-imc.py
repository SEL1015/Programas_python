#p005-calculadora-imc-py
#Calcular el IMC de una persona


print("Calculadora de Indice de Masa Corporal (IMC):\n")
peso_kg=float (input("Ingresa tu peso en kilogramos:"))
altura_m=float(input("Ingresa tu altura en metros:"))
imc=peso_kg/ altura_m**2 #**Operador artimetico Eleva un numero a una potencia 

print(f"Tu IMC ES: {imc:.2f}")
