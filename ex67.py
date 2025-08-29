from time import sleep

c = 0
while True:
    n = int(input("Digite um numero e veja sua tabuada: "))
    if n < 0:
        break
    for c in (range(0, 11)):
        print(n*c)
        sleep(0.2)

print("FIM")