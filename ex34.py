salarioAtual = float(input("Digite o salario atual do funcionário: "))
salarioNovo = 0
if(salarioAtual <= 1250):
    salarioNovo = (salarioAtual * (15/100)) + salarioAtual
    print(f"O salario novo é: R${salarioNovo}")
else:
    salarioNovo = (salarioAtual * (1/10)) + salarioAtual
    print(f"O salario novo é: R${salarioNovo}")
