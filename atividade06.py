numeros = []

for i in range(5):
    valor = float(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")