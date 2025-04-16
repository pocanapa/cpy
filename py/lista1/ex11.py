#Neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual
#de aumento. Você deverá escrever um algoritmo que recebe 2 números reais representando
#os salários antes e depois do aumento e deverá calcular e exibir o percentual de aumento que João obteve.

salarioAnt = float(input("Salario antes do aumento: "))

salarioAtual = float(input("Salario apos aumento: "))

porcentual = salarioAtual / salarioAnt - 1

print("O aumento foi de ", porcentual * 100)
