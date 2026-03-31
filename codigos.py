#algoritmo que receba três números inteiros e imprima o menor deles
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

#Verifique qual é o menor número
if a < b and a < c:
    print("O menor número é: ", a)
elif b < a and b < c:
    print("O menor número é: ", b)
else: 
    print("O menor número é: ", c)
print("Fim do algoritmo")    