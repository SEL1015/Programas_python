"""Escribe un programa con una función que reciba un número entero entre 1 y 7. La función debe devolver el día
de la semana correspondiente en texto (ej: 1 = "Lunes", 7 = "Domingo"). El programa principal debe pedir el
número al usuario, llamar a la función y mostrar el nombre del día.
Ejemplo de Ejecución:
Introduce un número del 1 al 7: 5
El día es: Viernes
Introduce un número del 1 al 7: 9
Error: El número debe estar entre 1 y 7."""
def dia_semana(numero: int) -> str:
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return dias.get(numero, "Error: El número debe estar entre 1 y 7.")
# Solicitar al usuario un número del 1 al 7
numero_usuario = int(input("Introduce un número del 1 al 7: "))         
# Llamar a la función y mostrar el resultado
resultado = dia_semana(numero_usuario)
print(f"El día es: {resultado}")

    