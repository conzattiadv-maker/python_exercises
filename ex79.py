val = list()
while True:
    v = int(input("Digite um valor na lista: "))
    if v not in val:
        val.append(v)
    else:
        print("Valor duplicado, não vou adicionar")
    opcao = str(input("Deseja continuar? [S/N]")).upper()
    if opcao == "N":
        break
print(f'Você digitou os valores {sorted(val)}')