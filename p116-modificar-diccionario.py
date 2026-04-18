# p116-modificar-diccionario.py
"""• Crea un diccionario llamado paises_dic con los siguientes pares (llave: valor): Argentina: 100, Brasil: 200,
Colombia: 300, Chile: 400, Ecuador: 500, Bolivia: 600, Jamaica: 700.
• Muestra el diccionario inicial.
• Modifica los valores de las siguientes llaves:
o Cambia el valor de Brasil a 250 (usando []).
o Cambia el valor de Chile a 450 (usando []).
o Cambia el valor de Bolivia a 650 (usando update()).
o Cambia el valor de Jamaica a 750 (usando update()).
• Muestra el diccionario modificado."""
print('\033[H\033[J')
# Crear el diccionario
paises_dic = { #se abre corchete de apertura de diccionario 
    'Argentina': 100,
    'Brasil': 200,
    'Colombia': 300,
    'Chile': 400,
    'Ecuador': 500,
    'Bolivia': 600,
    'Jamaica': 700
}

# Mostrar diccionario inicial todos los estados 
print("Diccionario inicial:")
print(paises_dic)

# Modificar valores usando []
paises_dic['Brasil'] = 250
paises_dic['Chile'] = 450

# Modificar valores usando update ()#la diferencia es que se hace con corchetes y entre parentesis usando ¨: para colocar el valor 
paises_dic.update({'Bolivia': 650})
paises_dic.update({'Jamaica': 750})

# Mostrar diccionario modificado ya con los valores solicitados 
print("\nDiccionario modificado:")
print(paises_dic)