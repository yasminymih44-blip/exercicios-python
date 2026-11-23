f = input("escreva a frase:").lower()
v = "aeiou"
contador = 0

for letra in f:
    if letra in v:
        contador += 1

print(f"o total de vogais é:{contador}")