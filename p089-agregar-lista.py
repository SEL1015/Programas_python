# p089-agregar-lista.py
# Agregar elementos a una lista
print('\033[H\033[J')
print('Agregar elementos a una lista')

#DECLARACION DE VARIABLES 
nums = [80.3, 12.5, 60.2, 30.4]


print(f'Agregar con append  90 y 100 al final:')
nums.append(90)
nums.append(100)
print(f'Datos  {len(nums)}- {nums}\n')


print(f'Insertar 80 en la posición 4:')
nums.insert(4, 80)
print(f'Datos  {len(nums)}- {nums}\n')


print(f'Externder datos agregando [110, 120, 130] se agregan al final:')
otros = [110, 120, 130]
nums.extend(otros)
print(f'Datos iniciales: {len(nums)}- {nums}\n')


#Append (): agrega un elemento al final de la lista 
# insert(): Inserta un elemento a una posicion especifica 
#Extend: fuciona una lista con otra ,agrega todos los elementos 