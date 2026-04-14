# p111-lote-autos.py
# Crear una lista de diccionarios para un lote de autos
print('\033[H\033[J')
autos = [
        { 'marca':'Ford', 'modelo':'Mustang', 'año': 1964 },
        { 'marca':'VW', 'modelo':'Jetta', 'año': 2005 },
]
autos.append({ 'marca':'Ford', 'modelo':'Focus', 'año': 2000 })
#Agrega elelemos a una lista append 

print('='*50) # 50 guiones 
print('Listado de Autos')
print('='*50)
print(f'\nTodos los autos : {autos} \nTotal: {len(autos)}')

#ciclo for primero uno luego el otro 
print('\nCada auto dentro de los autos:')
print('-'*50)
for auto in autos:
        print(auto)
print('\n Datos en forma de Tabla:')
print(" ")
print('-'*50)
for k in autos[0].keys():

        print(f'{k}\t', end='')
print('-'*50)

#ciclo cada auto en autos 
for auto in autos:
        for v in auto.values():
                print(f'{v}\t', end='')
        print("")
print('-'*50)

print('\nDatos en formato de Registro')
print('-'*50)
for auto in autos:
        for k,v in auto.items():
                print(f'{k:<12} : {v}')
        print('')
print('-'*50)