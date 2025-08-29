n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um núemro: "))

if(n1 > n2 and n1 > n3):
    if(n2 < n3):
        print("1° é o maior")
        print("2° é o menor")
    else:
        print("1° é o maior")
        print("3° é o menor")
elif(n2> n1 and n2 > n3):
    if(n1 > n3):
        print("2° é o maior")
        print("3° é o menor")
    else:
        print("2° é o maior")
        print("1° é o menor")
elif(n3 > n1 and n3 > n2):
    if(n2 > n1):
        print("3° é o maior")
        print("1° é o menor")
    else:
        print("3° é o maior")
        print("2° é o menor")