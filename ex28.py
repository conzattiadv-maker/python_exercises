from random import randint

n = randint(0, 5)
num = int(input("O computador pensou em um numero, qual é o numero: "))
if(num == n):
    print("Parabens!!")
else:
    print("EROOOU")