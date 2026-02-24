#p053-conjetura-collatz.py
# Calcula la conjetura de Collatz

while True:
    print("\033[H\033[J")
    print("Imprime la conjetura de collatz")

while True:
    num = int(input("Dame un número = "))
    if num > 1: break
p=0
while num !=1:
    print(num,end=" ")
    p+=1
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
print(num,end=" ")

print(f"Pasos llega a 1 : {p}")
if input("\n\nDeseas Continuar(S/N)? ").upper() =="N": break
print("\nGracias por usar este programa. Vuelve pronto.")

print("Proceso terminado ....")