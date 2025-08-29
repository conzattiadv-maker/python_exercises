from time import sleep
def maior(*num):
    cont = maior = 0
    print('\n\n', '-='*30)
    print("\nAnalizando os valores passados...")
    for valor in num:
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
        print(f"{valor}", end=" ")
        sleep(0.3)
    print(f"Foram encontrados {cont} numeros e o maior valor entre eles é {maior}")


maior(2, 5, 6, 2)
maior(1, 3, 6, 8)
maior(1, 2, 3)
maior(6)
maior()