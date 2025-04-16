time1 = input("Insira o nome do time: ")
time2 = input("Insira o nome do outro time: ")
gol1 = int(input("Quantos gols o primeiro time fez: "))
gol2 = int(input("Quantos gols o segundo time fez: "))

if gol1 > gol2:
    print(f"O {time1} ganhou a partida!")
    
elif gol2 > gol1:
    print(f"O {time2} ganhou a partida!")
else:
    print("Houve um empate!")