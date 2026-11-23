valor = int(input("Qual valor deseja sacar? R$ "))

if valor < 2 or valor == 3:
    print("Valor inválido! Não há cédulas disponíveis para esse valor.")
else:
    cedulas = [100, 50, 20, 10, 5, 2]
    print(f"\nSaque de R$ {valor}:")
    
    for cedula in cedulas:
        # Evita usar nota de 5 se o que sobrar depois dela for 1 ou 3 (ex: sacar 6 ou 8)
        if cedula == 5 and (valor % 5 == 1 or valor % 5 == 3):
            continue
            
        qtd_cedulas = valor // cedula
        if qtd_cedulas > 0:
            print(f"- {qtd_cedulas} cédula(s) de R$ {cedula}")
            valor = valor % cedula