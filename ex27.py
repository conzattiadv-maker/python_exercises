nome = str(input("Digite seu nome completo: ")).strip().lower()
nome = nome.split()
print(f"Primeiro nome: {nome[0]}")
print(f"Segundo nome: {nome[len(nome)-1]}")