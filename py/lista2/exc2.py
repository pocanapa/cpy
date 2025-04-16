#Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se
#houve um empate.

valor1 = int(input("Informe um numero: "))
valor2 = int(input("Informe um numero: "))

if valor1 > valor2:
    print(f"O maior valor é: {valor1}")
elif valor2 > valor1:
    print(f"O maior valor é: {valor2}")
else: 
    print("Os valores sao iguais. Houve um empate.")
