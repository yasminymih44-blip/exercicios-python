texto = input("Digite um parágrafo: ").lower()
palavras = texto.split()
contagem = {}

for p in palavras:
    contagem[p] = contagem.get(p, 0) + 1

for palavra, qtd in contagem.items():
    print(f"'{palavra}': {qtd}x")