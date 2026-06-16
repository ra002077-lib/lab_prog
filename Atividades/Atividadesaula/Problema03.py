palavra = input("Digite uma palavra: ").lower()
contador = 0
vogais = "a, e, i, o, u"

for caracter in palavra:
    if caracter in vogais:
        contador += 1

print(f"A palavra: {palavra}, tem {contador} vogais.")