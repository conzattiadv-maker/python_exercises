matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

i = 0
for l in range(0, 3):

    for c in range(0, 3):
        matriz[l][c] = int(input("Digite um número: "))
print(f'''
[{matriz[0]}]
[{matriz[1]}]
[{matriz[2]}]''')