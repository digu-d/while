import random

número_secreto = random.randint(1,10)

tentativa = 0

minimo = 1
maximo = 10

print("Tente adivinhar o número secreto de 1 entre 10")

while tentativa != número_secreto:
    tentativa = random.randint(minimo,maximo)
    print("Máquina tentou: ", tentativa)

    if tentativa < número_secreto:
        print("O número secreto e Maior")
        minimo = tentativa + 1
    elif tentativa > número_secreto:
        print("O número secreto e Menor")
        maximo = tentativa - 1
    else:
        print("Parabens!Voce acertou!!!")
