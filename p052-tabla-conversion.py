#p052-tabla-conversion.py

# Muestra una tabla de conversion de Peso a Dollar
#En un rango especifico 



tc= 19.70
while True : #Mientras que cierto 
    print('\033[H\033[J')#Borrar pantalla
    print("Tabla de Conversion Peso a Dollar")

    print(f'Tipo de Cambio: {tc} Pesos por Dollar')
    while True:
        pi = float(input("Valor inicial: "))
        pf = float(input("Valor final : "))
        
        if (pi>0 and pf>0) and pi<pf: break
        print("*")
        print("Error en los valores, intente de nuevo")
c = pi
print("\nPesos\tDollar")
print("-"*30)
while c<=pf:
    print(f'{c:>10}\t{c/tc:>10.2f}')
    c= c+1
print("-"*30)
if input('Deseas Continuar(S/N)? ').upper() =='N' :  break

