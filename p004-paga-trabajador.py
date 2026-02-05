#p004-paga-trabajador.py
#Calcular la paga total de un trabajador 


print("Calcular la paga de un trabajador")
#Entrada
print("Nombre:")
nombre=input()
print("Horas trabajadas:")
horas=int(input())
print("Paga por hora:")
paga= float(input())

#Proceso
tasa= 0.3
pagabruta=horas*paga
impuesto=pagabruta*tasa
paganeta=pagabruta-impuesto

#Salida
print("Resumen de pagos:\n")
print(f"El trabajador {nombre}, trabajo {horas} , con una paga de {paga} pesos por hora, impuesto de {tasa} %")
pr(f"paga: {pagabruta}")
print(f"impuesto : {impuesto}")
print(f"paga neta: {paganeta}")

