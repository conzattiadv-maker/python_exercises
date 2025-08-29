qtdKm = float(input("Digite quantos km foram rodados: "))
qtdDias = int(input("Digite a quantos dias alugou o carro: "))
dias = 60
km = 0.15
valorF = qtdKm*km+qtdDias*dias
print(f"Você me deve R${valorF} calotero")