n = int(input("digite um ano: "))
b = n % 4

if(b == 0):
    print(f"O ano {n} é bissexto")
else:
    print(f"O ano {n} não é bissexto")