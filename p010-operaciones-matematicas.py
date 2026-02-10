#p010-operaciones-matematicas.py
#Demuestra el uso de los diferentes operadores artimeticos 

print("\033[h\033[j")#imprime una secuencia ansi que borra la pantalla]]")

print("="*50)
print("CALCULADROA DE OPERACIONES MATEMATICAS")
print("="*50)

x=float(input("Dame el valor de x: "))
y=float(input("Dame el valor de y:"))

print(f"Los valores de x y y son {x} {y}")
print("-"*40)

#Mostar resultados de las operaciones directamente , con formato alienado 
print(f"Suma:   {x:>6} +   {y:>6}         =    {x+y:>10.2f}")
print(f"Resta:  {x:>6} -   {y:>6}         =    {x-y:>10.2f}")
print(f"Mult:   {x:>6} *   {y:>6}         =    {x*y:>10.2f}")
print(f"Div:    {x:>6} /   {y:>6}         =    {x/y:>10.2f}")
print(f"Mod:    {x:>6} %   {y:>6}         =    {x % y:>10.2f }")
print(f"Exp:    {x:>6} **  {y:>6}         =    {x ** y:>10.2f }")
print(f"Div E : {x:>6} //  {y:>6}         =    {x // y :>10.2f}")
print("-"*40)


