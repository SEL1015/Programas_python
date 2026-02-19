# p048-multiplos-continue.py
# Imprime solo los múltiplos de 10 hasta 200.
print(" Imprime los multiplos  de n  a 200...")
print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]")

n= int(intput("Que multiplos quieres hasta 200"))
c = 0

while c < 200:
    c += 1
if c % n != 0:
# "Ignora todo lo que sigue y salta a la siguiente iteración".
    continue
# Esta línea SÓLO se ejecuta si el 'if' fue falso (es decir, si es un múltiplo de 10).
print(f" {c}", end=" ")

print("\n Búsqueda finalizada.")