# p127-funcion-parametro.py
print('\033[H\033[J')
def saluda(nombre: str) -> None:

    print(f'Hola {nombre} bienvenido a Python, tu nombre tiene {len(nombre)} caracteres')

saluda('Carlos Castaneda')
saluda('Juan Perez Diaz')
saluda('María Soto García')