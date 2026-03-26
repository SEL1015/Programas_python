#p105-datos-estudiante
#Ejemplifica las operaciones sobre un diccionario 

print('\033[H\033[J')
print(" Gestion de estuidante")


estuidante= {"nombre:"uan Prerez", "edad":"45",-mail":"jperez@.com","carrera": "sistemas"}

print(f"Diccionario : {estudiante}- {len(estudiante)}")

estudiante["calificacion"]=9.5
estudiante["e-mail"]= "juanp@gmail.com"
print(f"Diccionario :{estudiante}- {len(estudiante)}")
print('\nLas llaves del diccionario: \n')
for k in estudiante.keys():
print(k)

print('\nLos valores del diccionario: \n')
for v in estudiante.values():
print(v)

print("\nListado de llaves y valores:\n")
for k, v in estudiante.items():
print(f'{k:<10} : {v}')


