temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    resp = str(input("Continuar (S/N): ")).upper()
    temp.clear()
    if resp == 'N':
        break
print("-=" * 30)
print(f"Ao todo você cadastrou {len(princ)} pessoas")
print(f"O maior peso é {mai}kg. Peso de ", end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f"\nO menor peso é {men}kg. Peso de", end=' ')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
print()