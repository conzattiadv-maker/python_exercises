l1 = float(input(f"Digite o tamanho do 1° lado do triângulo: "))
l2 = float(input(f"Digite o tamanho do 2° lado do triângulo: "))
l3 = float(input(f"Digite o tamanho do 3° lado do triângulo: "))
if l3 < l1 + l2 and l1 < l2 + l3 and l2 < l1 + l3:
    print("Com esses seguimentos, SIM é possível formar um triangulo.")
else:
    print("NÃO é possivel formar um triangulo.")