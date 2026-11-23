p = input("Digite uma palavra: ").replace(" ", "").lower()
i = p[::-1]

if p == i:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")