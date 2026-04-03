#Algoritmo que leia um número 
a = float(input("Digite um número: "))

#Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário, informe “Número inválido”
if (a >= 0):
    print("A raiz aproximada do número é: ", a ** 0.5)
else: 
    print("Número inválido")
print("Fim do programa")        