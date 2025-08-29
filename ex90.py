aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Media de {aluno['nome']}\n"))
if aluno['media'] <= 7.0:
    aluno['resp'] = "Reprovado"
else:
    aluno['resp'] = "Aprovado"
print(f"Nome é igual a {aluno['nome']}\n"
      f"Media é igual a {aluno['media']}\n"
      f"Situação é igual a {aluno['resp']}\n")