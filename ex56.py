nomeHomemV = ' '
idadeHomemV = 0
media = 0
somaIdade = 0
qtdM = 0
for c in range(1, 5):
    print(f"{5*'-'}{c}° pessoa")
    nome = str(input("Nome: ")).strip()
    idade = float(input("Idade: "))
    sexo = str(input("Sexo [M/F]")).strip()
    somaIdade += idade
    if c == 1 and sexo in "Mm":
        idadeHomemV = idade
        nomeHomemV = nome
    if sexo in "Mm" and idade > idadeHomemV:
        idadeHomemV = idade
        nomeHomemV = nome
    if  sexo in "Ff" and idade < 20:
        qtdM += 1

media = somaIdade/4
print(f"A media de idade é de: {media}")
print(f"O homem mais velho do grupo se chama {nomeHomemV} com {idadeHomemV} anos")
print(f"O grupo possui {qtdM} mulheres com menos de 20 anos")