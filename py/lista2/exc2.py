#Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se
#houve um empate.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    diferenca = valor1 - valor2
else:
    diferenca = valor2 - valor1

print("A diferença entre os valores é: ", diferenca)
