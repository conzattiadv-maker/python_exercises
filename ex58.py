from random import randint
from time import sleep

n = randint(0, 10)
num = -1
while num != n:
    num = int(input("O computador pensou em um numero, qual é o numero: "))
    if (num == n):
        print("Parabens!!")
    else:
        print("Que pena. Tente novamente ")
        sleep(0.8)


