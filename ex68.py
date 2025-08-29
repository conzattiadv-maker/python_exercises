from random import randint
vitoria = 0
while True:
    computadorNUM = randint(1, 2)
    IP = int(input("[1]imar ou [2]par"))
    n = int(input("Escolha um numero"))
    if IP == 1:
        if (n + computadorNUM) % 2 == 0:
            print("Voce perdeu ")
            break
        else:
            vitoria += 1
    elif IP == 2:
        if (n+ computadorNUM) % 2 == 1:
            print("Você perdeu ")
            break
        else:
            vitoria += 1
print(f"Você venceu {vitoria} vez(es)")