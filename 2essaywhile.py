import random

limite = int(input("Até qual número posso sortear para voce: "))

chances = int(input("Quantas chances voce gostaria de possuir: "))

numero_secreto = random.randint(1, limite)

acertou = False

while chances > 0:
    print("Voce tem: ",chances, "chances")
    tentativa = int(input("Tente adivinhar o número secreto: "))

    if tentativa == numero_secreto:
        print("Parabens Voce acertou fim de jogo")
        acertou = True
    elif tentativa > numero_secreto:
        print("O numero secreto e menor")
    else:
        print("O numero secreto e maior")

    chances -= 1

if not acertou:
    print("Suas chances acabaram")
    print("O numero secreto era: ", numero_secreto)
