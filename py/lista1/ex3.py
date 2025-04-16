#Escreva um algoritmo que recebe o nome de uma pessoa e seu ano de nascimento. Seu
#algoritmo deverá mostrar na tela o nome da pessoa e a idade que ele tem ou terá até o fim
#de 2024. Por exemplo, supondo que a pessoa informe o ano de nascimento como 1986 seu
#programa deverá imprimir:
#Fulano de tal tem (ou terá) 34 anos

nome = input("Digite o nome: ")
aux = input("Digite o ano de nascimento: ")

#convertendo aux para número inteiro
ano = int(aux)

idade = 2025 - ano

print(nome, "tem ou terá", idade, "anos")