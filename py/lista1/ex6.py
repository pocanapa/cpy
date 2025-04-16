#Escreva um algoritmo que calcula a área e o perímetro do círculo, 
# use 3.141592 como valor de π.

# Definir a constante pi

pi = 3.141592

# Solicitar o raio ao usuário

raio = float(input("Digite o raio da circunferência: "))

# Calcular a área da circunferência

area = pi * (raio ** 2)

# Exibir o resultado

print(f"A área da circunferência é: {area}")