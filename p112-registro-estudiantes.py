# p112-registro-estudianteudiantes.py
# Crear una lista de diccionarios para representar un registro de estudianteudiantes
print("\033[H\033[J")
grupo = [
{"nombre":"Carlos","edad":45,"carrera":"sistemas","promedio":9} ,
{"nombre":"Rocio","edad":35,"carrera":"sistemas","promedio":10}
]

print("\n Registro de estudianteudiantes\n")

print(f"\nGrupo de estudianteudiantes inicial:\n{"-"*60}\n{grupo} - {len(grupo)}")
#el usuario capruta los datos
print("\nCaptura de nuevos estudianteudiantes")
print("-"*60)
#ciclo while para capturar datos 
while True:
    print(f"Datos estudianteudiante:")
    datos = {} #sin datos vacio 
nombre = input("Nombre ? ")
if nombre == "":
    break
datos["nombre"] = nombre
datos["edad"] = int(input("Edad? "))
datos["carrera"] = input("Carrera ? ")
datos["promedio"] = float(input("Promedio? "))
grupo.append(datos) # agregar la lista al diccionario 


print(f"\nGrupo de estudianteudiantes completo:\n{"-"*60}\n{grupo} - {len(grupo)}")

print("\nDatos en forma de Tabla:")
print("-"*60)
for k in grupo[0].keys():

    print(f"{k:<13}", end="")
print()

for alumno in grupo:
    for v in alumno.values():
        print(f"{v:<13}", end="")
print()
#Datos en forma de registro
print("\nDatos en forma de Registro ")
print("-"*60)
s=0
for estudiante in grupo:
    s+= estudiante["promedio"]
for k,v in estudiante.items():
    print(f"{k:<10} : {v}")
print()


print("\nCálculo de Promedios:")
print("-"*60)
p = s / len(grupo)
print(f"La suma es {s}")
print(f"El promedio es {p:.2f}")