import math

catetoO = float(input("Digite o valor do cateto oposto: "))
catetoA = float(input("Digite o valor do cateto adjacente: "))

hipo = math.hypot(catetoO, catetoA)
print(f"O Cumprimento da hipotenuza é {hipo:.2f}")