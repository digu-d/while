import random

vida1 = random.randint(1,75)
vida2 = random.randint(1,75)

atk1 = random.randint(1,15)
atk2 = random.randint(1,15)

print("Jogador 1 vida ->:", vida1, "Ataque:", atk1)
print("Jogador 2 vida ->:", vida2, "Ataque:", atk2)

turno = random.choice([1,2])
print("O Jogador que começa é: Jogador", turno)

while vida1 > 0 and vida2 > 0:
    if turno == 1:
        vida2 -= atk1
        print("O Jogador 1 atacou,Vida do jogador 2: ", vida2)
        turno = 2
    else:
        vida1 -= atk2
        print("O Jogador 2 atacou,Vida do jofador 1: ", vida1)
        turno = 1

print(" !!!--- FIM DE JOGO ---!!!")
if vida1 <= 0:
    print("O Jogador 2 venceu!")
else:
    print("O Jogador 1 venceu!")     
