numeros = [[],[]]
while True:
    valor = int(input("Digite um número: "))
    if valor % 2 == 1:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
    resp = str(input("Deseja continuar (S/N): ")).upper()
    if resp == "N":
        break


print(f'Os numeros impares são: {sorted(numeros[0])}\nOs numeros pares são {sorted(numeros[1])}')