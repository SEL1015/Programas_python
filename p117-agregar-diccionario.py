#p117-agregar-diccionario.py
"""Crea un diccionario llamado ventas con los siguientes datos: Juan: 1550, Jose: 2600, Maria: 2220.
• Muestra el diccionario.
• Agrega los siguientes vendedores y sus ventas al diccionario:
o Rocio: 2500 (usando []).
o Mateo: 1567 (usando []).
o Andrea: 9567 (usando update()).
o Miguel: 1234 (usando update()).
• Muestra el diccionario actualizado."""
print('\033[H\033[J')
# Crear el diccionario
nombres = { #se abre corchete de apertura de diccionario 
    'Juan': 1550,
    'Jose': 2600,
    'Maria': 2220,
}
#Agregar usando (usando []).
nombres['Rocio'] = 2500
nombres['Mateo'] = 1567
print(nombres)
#Agregar (usando update()).
otros = {'Andrea': 9567, 'Miguel ': 1234}

nombres.update(otros)

print(nombres)