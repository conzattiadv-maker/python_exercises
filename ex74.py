from random import randint
maior = 0
menor = 0
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
for c in range(0, 5):
    print(f'{n[c]}',  end=" ")
    if c == 0:
        maior = n[c]
        menor = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
print(f"O maior valor é {maior} e o menor valor é {menor}")