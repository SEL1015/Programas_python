# p074-suma-mutiplos.py
# Suma de nuerms introducidos por el usuario usando for 

while(True):
    print('\033[H\033[J')

    cuantos = int(input('Cuantos numeros deceas procesar  ? '))
    suma =0
    cadnum=""

    for i in range(1, cuantos+1):
        n=float(input(f"Numero {i} / {cuantos}"))
        suma=suma+n
        cadnum=cadnum+" "+ str(n)
    
    print(f'\nLos numeros son   {cadnum}')
    print(f'\nLa suma es  {suma}')
    print(f'\nel promedio  es  {suma/cuantos:.2f}')

    if input('\n\nDeseas continuar (S/N) ? ').upper()=='N': break
print('\nHemos llegado al final ....')