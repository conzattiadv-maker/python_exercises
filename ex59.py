from contextlib import nullcontext
from time import sleep
n = 0
def soma(a, b):
    s = a + b
    return s
def mult(a, b):
    m = a * b
    return m
def maior(a, b):
    if a > b:
        print("O maior numero é o primeiro}")
    elif b > a:
        print("O maior é o segundo")
    else:
       print("Os dois são iguais.")
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
while n != 5:
    print(f"""
        {"="*10}
        [1]somar
        [2]multiplicar
        [3]maior
        [4]novos números
        [5]sair do programa
    """)
    n = int(input("Qual é a sua opcão?\n"))
    if n == 1:
        print(f"A soma de {n1} + {n2} é igual a {soma(n1, n2)}")
    elif n == 2:
        mult(n1, n2)
        print(f"A multiplicação de {n1} * {n2} é igual a {mult(n1, n2)}")
    elif n == 3:
        maior(n1, n2)
    elif n == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))

    sleep(1)
print("!!!FIM!!!")