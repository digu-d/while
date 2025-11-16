import random

número_secreto = random.randint(1,10)

tentativa = 0

print("Tente adivinhar o número secreto de 1 entre 10")

while tentativa != número_secreto:
    tentativa = int(input("Digite seu palpite: "))

    if tentativa < número_secreto:
        print("O número secreto e Maior")
    elif tentativa > número_secreto:
        print("O número secreto e Menor")
    else:
        print("Parabens!Voce acertou!!!")
