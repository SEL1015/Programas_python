"""
p069 - Primer examen parcial
Carlos Héctor Castañeda Ramírez

11:42 a.m. (Editado: 12:00 p.m.)
Examen
10 puntos
Fecha límite: Mañana, 11:59 p.m.
Primer Examen Parcial de Computación Aplicada
Resuelve el problema planteado en el pdf anexo.
Usa la plantilla como base para la solución (obligatorio).
Contesta las preguntas al final de la plantilla, pon las respuestas ahí mismo.
Dar al examen el nombre de: p066-primer-parcial.py
Anexar como entrega el URL al repositorio.
Notas:
Para la solución del examen, solo usar lo que se ha visto en clase (if,  if .. elif .. else , while )
No usar sentencias o instrucciones no vistas (for, arreglos, funciones, etc. )
Preferentemente no usar IA para resolverlo, si te apoyas en IA trata de entender lo que se hizo, al final se trata de aprender, la IA ya lo sabe hacer, lo sabes hacer tu ?
09-PirmerExamenParcial.pdf
PDF

p066-plantilla.py
Texto

Comentarios de la clase
Tu trabajo
Asignado
Comentarios privados
"""
"""
Objetivo: [VENTA DE BOLETOS EN EL CINE ]
Nombre del Alumno: [SELENA RUIZ DELGADO ]
Matrícula: [43427121]
Materia: Computación Aplicada
Examen: Primer Parcial
"""
# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos

# --- Contadores de Asistentes ---
total_estudiante = 0
total_adulto=0
total_tercera_edad=0
total_academico=0
total_mujeres=0
total_hombres=0


# ... (agrega los demás contadores de tipo de comprador y de sexo)

total_asistentes = 0
total_rechazados = 0
suma_edades = 0

# --- Acumuladores de Ingresos ---
ingresos_estudiante = 0.0
ingresos_adulto=0
ingresos_tercera_edad=0
ingresos_academico=0
# ... (agrega los demás acumuladores de ingresos)

ingresos_totales = 0.0

# --- Precios de los Boletos (constantes) ---
PRECIO_ESTUDIANTE = 50.0
PRECIO_ADULTO = 90.0
PRECIO_TERCER_EDAD=60.0
PRECIO_ACADEMICO=70.0

# ... (agrega las demás constantes de precios)

print('\033[2J\033[H')
print("---🍿🍿🍿🍿🍿 Sistema de Venta de Boletos de Cine 🍿🍿🍿🍿🍿🍿---")

# --- Ciclo Principal para la Venta de Boletos ---
# Usaremos un ciclo while para registrar ventas hasta que el usuario decida parar.
continuar_venta = "s"
while continuar_venta == "s":

    print("\n---🎟️🎟️🎟️🎟️ Nueva Venta 🎟️🎟️🎟️🎟️---")
    # --- 1. Solicitud de Datos ---
    # Pide la edad, el tipo de comprador y el sexo.
    # ¡Recuerda convertir la edad a un número entero!

    edad = int(input("Ingrese la edad del comprador: "))
    
    # --- 2. Validación de Edad (Clasificación B) ---
    # La película es para mayores de 13 años.
    if edad >13:
        # Si la edad es permitida, procede con la venta.
        # Muestra el mensaje de bienvenida con los datos registrados
        tipo = input("Tipo (Estudiante/Adulto/Tercera Edad/Académico): ") 
        sexo = input("Sexo (Hombre/Mujer): ")
        print(f"¡Bienvenido(a)!Venta registrada ... {edad} , Sexo : {sexo}, Tipo :  { tipo}")
        # --- 3. Actualización de Estadísticas Generales ---
        # Incrementa el contador de asistentes y suma la edad para el promedio.
        # Incrementa el contador de sexo correspondiente (hombre o mujer).
        if sexo == "Hombre":
            total_hombres = total_hombres + 1
        else:
            total_mujeres = total_mujeres + 1
            total_asistentes = total_asistentes + 1
            suma_edades = suma_edades + edad
        # --- 4. Cálculo de Costo y Actualización de Contadores Específicos ---
        # Usa una estructura if/elif/else para determinar el precio y actualizar
        # los contadores del tipo de comprador y sus ingresos.
        # Suma el costo del boleto a los ingresos totales.
        
        
        # Contador por tipo e ingresos
        if tipo == "Estudiante":
            total_estudiante = total_estudiante + 1
            ingresos_estudiante = ingresos_estudiante + 50
        elif tipo == "Adulto":
            total_adulto = total_adulto + 1
            ingresos_adulto = ingresos_adulto + 90
        elif tipo == "Tercera Edad":
            total_tercera_edad = total_tercera_edad + 1
            ingresos_tercera_edad = ingresos_tercera_edad + 60
        elif tipo == "Académico":
            total_academico = total_academico + 1
            ingresos_academico = ingresos_academico + 70
            ingresos_totales = ingresos_estudiante + ingresos_adulto + ingresos_tercera_edad + ingresos_academico
        
    else:
        # Si la edad no es permitida, muestra un mensaje y actualiza el contador ()
        print("ACCESO DENEGADO: El comprador es menor de 13 años.")
        total_rechazados = total_rechazados + 1
    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()

# --- FIN DEL CICLO ---

# --- 5. Cálculo de Promedio ---
# Calcula el promedio de edad. Cuidado con la división entre cero si no hubo asistentes.
promedio_edad = 0 #Aqui declare la variable en 0 
if total_asistentes > 0:
    promedio_edad = suma_edades / total_asistentes
else:
    promedio_edad = 0
total_general = ingresos_estudiante + ingresos_adulto + ingresos_tercera_edad + ingresos_academico
# --- 6. Impresión del Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")
print("--------------------------------------------------------------------")

print("\n--- Estadísticas del Público ---")
# Imprime todos los totales de asistentes por tipo y sexo.
print(f"Total de Estudiantes         {total_estudiante}")
print(f"Total de Adultos             {total_adulto}")
print(f"Total de Tercera Edad        {total_tercera_edad}")
print(f"Total de Academicos          {total_academico}")
print(f"Total de Hombres             {total_hombres}")
print(f"Total de Mujeres             {total_mujeres}")
print(f"Total de Asistentes          {total_asistentes}")
print(f"El promedio de la edad es :  {promedio_edad}")
print(f"Total de Rechazados fueron : {total_rechazados}")

print("\n--- Reporte de Ingresos ---")
# Imprime todos los ingresos por tipo de comprador y el total general.
# Utiliza formato para mostrar  dos decimales en el dinero.4
print(f"Total de dindero recaudado Estudiantes  :   $   {ingresos_estudiante:.2f}")
print(f"Total de dindero recaudado Adultos :        $   {ingresos_adulto:.2f}")
print(f"Total de dindero recaudado Tercera Edad :   $   {ingresos_tercera_edad:.2f}")
print(f"Total de dindero recaudado Academicos :     $   {ingresos_academico:.2f}")
print(f"Total de dindero recaudado en General:      $   {total_general:.2f}")


print("\n--- Rentabilidad ---")
# --- 7. Mensaje de Rentabilidad ---
# Usa una estructura if/elif/else para determinar si las ganancias
# fueron BAJAS, MODERADAS o BUENAS, basándote en los ingresos totales.
if total_general < 1500:
    print("La función generó BAJAS ganancias.")
else:
    if total_general <= 3500:
        print("La función generó ganancias MODERADAS.")
        if total_general >3500:
            print("La función generó BUENAS ganancias.")
        else:
            print("No fue tu dia ")

"""

Preguntas: Explica con tus palabras

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

[1.- Agrgar una condicion que si el usuario ingresa "Martes" , se condiciona a que se aplique el 20 % de descuento 
 2.- La nueva pregunta seria que ¿ingresare el dia de la funcion? y verificar que  si es adulto , pasaria en automatico al descuento 
 3.- #Declarar la variable nueva que almacenara el dia que ingrese 
 dia = input("Ingrese el día de la función: ").lower()
 if tipo == "Adulto":
    total_adultos = total_adultos + 1

    if dia == "martes":
        ingresos_adulto = 90 * 0.80   # es la funcion para aplicar el 20% descuento
    else:
        ingresos_adulto = 90]

2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
aunque los ingresos por cada tipo de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

[Verificaria primero si la variable asignada a la suma de los totales esta bien definida y escrita al momento de solicitar el reporte final

total_general = ingresos_estudiante + ingresos_adulto + ingresos_tercera_edad + ingresos_academico # En este apardado verificaria que si este correcto para que sume adecuadamente cada precio ingresado de cada cliente del cine  ]
"""
