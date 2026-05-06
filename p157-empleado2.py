# p157-empleado2.py
# Clase empleado con propieades adicionales
# Código de clase

print('\033[H\033[J')
class Empleado:
    def __init__(self, nombre, edad, sexo, casado):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.casado = casado
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {"Mujer" if self.sexo == "M" else "Hombre"}, Casado: {"Casado" if self.casado else "No Casado"}'

# Programa principal
emp1 = Empleado('Jose Diaz', 35, 'H', True)
print('Nombre: ', emp1.nombre)
print('Edad : ', emp1.edad)
print('Sexo : ', emp1.sexo)
print('Casado: ', emp1.casado)
print(emp1)