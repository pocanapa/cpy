#Sua tarefa é desenvolver um algoritmo que recebe um número inteiro de 0 a 99 e imprime o
#dígito das dezenas e o dígito das unidades desse número. Dica: usando papel e lápis faça a
#divisão inteira do número por 10 mas não coloque vírgula e nem acrescente 0 na divisão.

num = int(input("Digite um número: "))
dez = num // 10
uni = num % 10
print('Dezena: ', dez)
print("Unidade: ", uni)

print(f"Dezena = {dez}")
print(f"Unidade = {uni}")
