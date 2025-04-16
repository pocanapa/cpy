#Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. Escreva
#um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. Seu algoritmo
#deverá ler o número de camisas, o número de calças e o número de pares de sapato.

camisa = input("Informe quantas camisas tem: ")
x = int(camisa)

calcas = input("Informe qunatas calças tem: ")
y = int(calcas)

sapatos = input("Informe quantos pares de sapato tem: ")
z = int(sapatos)

soma = x * y * z

print(soma, "maneiras diferentes")               