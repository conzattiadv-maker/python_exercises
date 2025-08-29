frase = str(input("DIgite uma frase: ")).strip().lower()
print(f"A letra A aparece {frase.count('a')} vezes")
print(f"A primeira letra A é vista na {frase.find('a')+1}")
print(f"A ultima ocorrência da letra A foi na {frase.rfind('a')+1}° posição")
