multa = 0
vel = float(input("Digite a quantos km/h estava o veiculo: "))
if(vel>=80):
    vel = vel-80
    multa = vel * 7
    print(f"O valor da multa por ultapassar 80km é de R${multa:.2f}")
else:
    print(f'você esta dentro dos limites abaixo de 80 com {vel}km/h')