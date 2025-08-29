#R$0.5 <= 200, 0.45 > 200
km = float(input("Digite a distancia em km: "))
if(km <= 200):
    valor = km * 0.5
else:
    valor = km * 0.45
print(f"O valor da viagem de {km} é de R${valor}")