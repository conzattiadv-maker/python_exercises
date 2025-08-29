valor_Da_Casa = float(input("Digite o valor da casa: \nR$"))
salario = float(input("Digite o valor do salario mensal: R$"))
anos_de_Pagamento = int(input("Em quantos anos deseja pagar a casa: "))
ano = anos_de_Pagamento * 12
prestacao_Mensal = valor_Da_Casa / ano
if prestacao_Mensal < (salario*0.3):
    print(F"Certo...Seu empréstimo de R${prestacao_Mensal:.2F} sera liberado em alguns instantes.")
else:
    print(f"Recusado...Não é possível fazer o empréstimo de R${prestacao_Mensal:.2F}")