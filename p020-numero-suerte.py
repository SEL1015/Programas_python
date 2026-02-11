#p020-numero-suerte
#Escribe un programa que solicite al usuario su año de nacimiento como un número entero de cuatro dígitos. A partir 
#de este dato, el programa debe: 
#Mostrar cada uno de los dígitos individuales del año. Por ejemplo, si el año es 1995, debe mostrar "1", "9", 
#"9", "5".  
# Calcular y mostrar la suma de los dígitos individuales del año. Siguiendo el ejemplo anterior, la suma sería 
#1 + 9 + 9 + 5 = 24. 

#Entrada
print("Calcular el numero de la suerte a partir del año de nacimiento")

#Se solicita el año de nacimiento al usuario 

ano_nac=int(input("Ingrese su año de nacimiento de 4 digitos "))


#Calcular los digitos individuales del año de nacimiento obtenidos separados por espacio
digiton1,digiton2,digiton3,digiton4=ano_nac//1000, (ano_nac%1000)//100,(ano_nac%100)//10, ano_nac%10

#Calcular la suma de los digitos individuales del año de nacimiento 

print(f"Los digitos individaules del año de nacimiento son {digiton1} , {digiton2}, {digiton3}, {digiton4}")

suma_de_digitos= digiton1+digiton2+digiton3+digiton4
print(f"La suma de los digitos individuales del año es : {suma_de_digitos}")

