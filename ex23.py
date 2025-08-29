num = int(input("Digite um numero:\n"))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Analizando numero {num}\n")
print(f"""
Unidade {u}
Dezena {d}
Centena {c}
Milhar {m}""")