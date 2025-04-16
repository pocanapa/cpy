#Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula
#e mostra o valor do desconto e o novo preço do produto dado o percentual. E se, ao invés
#de um desconto, fosse um aumento.
#O que muda no seu algoritmo?

preco = float(input("Digite o preco do produto: "))

desconto = float(input("Informe o percentual de desconto: "))

valorDesconto = preco * desconto / 100

precoComDesconto = preco - valorDesconto

print("O valor do desconto e de ", valorDesconto)
print("O novo preco e de ", precoComDesconto)
