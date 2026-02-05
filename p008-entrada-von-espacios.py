#p008-entrada-con-espacios.py
#Leer tres numeros enteros con espacio 

print("Dame cuatro numeros separados por un espacio")

n1,n2,n3,n4=input().split()
n1,n2,n3,n4=int(n1), int(n2), int(n3), int(n4)

print(f"Los valores introducidos fueron: {n1},{n2},{n3},{n4}")

print(f"La suma de los numeros es: {n1+n2+n3+n4}")
