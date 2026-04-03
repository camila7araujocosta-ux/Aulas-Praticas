#Algoritmo que leia dois números 
a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))

#Mostre qual número é o maior 
if (a > b):
    print("O número", a ,"é maior que o número", b)
elif (b > a):
    print("O número", b , "é maior que o número", a)
else:
    print("Os números são iguais")
print("Fim do programa")           