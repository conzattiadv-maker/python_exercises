texto = str(input("Digite o nome da sua cidade: "))
texto = texto.upper().strip()
print(f"{texto[:5] == 'SANTO'}")