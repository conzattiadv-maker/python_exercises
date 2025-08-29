import math
n = int(input("Digite um numero inteiro: "))
print("""
Escolha uma base de conversão:
[1]-Binario
[2]-Octal
[3]-Hexadecimal
""")
opcao = int(input("Escolha:"))
if opcao == 1:
    print(f'O numero {n} em binario é {bin (n)}')
elif opcao == 2:
    print(f'O numero {n} em Octal é {oct (n)}')
elif opcao == 3:
    print(f'''O numero {n} em Hexadecimal é {hex (n)}


''')
else:
    print("Numero invalido!!!!!")
