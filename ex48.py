a = 0
b = 0
for c in range(1, 501, 2):
    if c % 3 ==0:
        a = a + c
        b+=1

print(f"A soma de todos os {b} valores é de {a}")