#O RM de um aluno da FIAP é composto por 5 dígitos. Sua tarefa é escrever um algoritmo que
#recebe um RM e retorna a somatória de todos os dígitos do RM. Por exemplo, suponha que
#o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5 + 6 + 3 + 9 + 5.

#Dica: realize várias divisões e restos de divisões por 10.

rm = int(input("Informe o RM: "))
soma = 0

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

print(soma)