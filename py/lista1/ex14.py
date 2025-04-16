#As casas de São Paulo estão recebendo o carnê do IPTU com duas opções de pagamento:
#à vista ou em 10 vezes. Sua tarefa é desenvolver um programa/algoritmo onde o usuário
#informa (digita) o valor total à vista e o valor de cada parcela. Seu programa imprime o
#desconto em percentual dado pela prefeitura para pagamento à vista.

avista = float(input("Informe valor do iptu a vista: "))

parcela = float(input("Informe valor da parcela: "))

aprazo = parcela * 10

porcentual = 1 - avista / aprazo

print("O valor do desconto foi de ", porcentual * 100)
