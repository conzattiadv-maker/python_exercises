from time import sleep

def contador(i, f, p):
    print(f"Contador de {i} até {f}, de {p} em {p}")

    cont = i
    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    if i >= f:
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
            sleep(0.3)
        print("FIM")
    else:
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
            sleep(0.3)
        print("FIM")


contador(1, 10, 1)
contador(10, 0, 2)
print("-="*30)
print("Agora é sua vez!!!")
ini = int(input("Inicio: "))
fim = int(input("Fim:    "))
pas = int(input("Passo:  "))

contador(ini, fim, pas)
print('-='*30)