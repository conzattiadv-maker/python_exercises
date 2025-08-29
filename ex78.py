vals = list()
maior = 0
menor = 0
for c in range(0, 5):
    vals.append(int(input(f"Digite o numero {c+1}: ")))
vals.sort(reverse=True)
print(vals)
menor = vals[4]
maior = vals[0]
print(f"O maior valor é {maior} e o menor valor é {menor}")