#Escreva um algoritmo em Python que recebe dois números inteiros e exibe: a soma desses
#dois números, a multiplicação, a divisão inteira e o resto da divisão inteira.


aux = input("Digite a: ")
num_a = int(aux)
aux = input("Digite b: ")
num_b = int(aux)

soma = num_a + num_b
produto = num_a * num_b
divisao = num_a // num_b
resto = num_a % num_b

print(f"{num_a} + {num_b} = {soma}")
print(f"{num_a} * {num_b} = {produto}")
print(f"{num_a} // {num_b} = {divisao}")
print(f"{num_a} % {num_b} = {resto}")









