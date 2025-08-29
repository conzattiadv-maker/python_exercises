from datetime import datetime
dados = dict()
dados['nome'] = str(input("Nome: "))
dados['ano'] = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - dados['ano']
dados['carteira de trabalho'] = int(input("Carteira de trabalho (0 se não tem): "))
if dados['carteira de trabalho'] != 0:
    dados['anoContratado'] = int(input("Ano de contratação"))
    dados['salario']= int(input("Salario: R$"))
    dados['aposentadoria'] = dados['idade'] + ((dados['anoContratado'] + 35) - datetime.now().year)
    print(f'''Nome: {dados['nome']}
    Idade: {dados['idade']}
    Ctps: {dados['carteira de trabalho']}
    Contratação: {dados['anoContratado']}
    Salário: R${dados['salario']}
    Aposentadoria: {dados['aposentadoria']}\n''')
else:
    print(f'''Nome: {dados['nome']}
        Idade: {dados['idade']}
        Ctps: {dados['carteira de trabalho']}''')