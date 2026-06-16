historico = []
valor = 1
print("===Simulador Fluxo de Caixa===")
while valor != 0:
    valor = float(input("Digite o Valor (0 para sair): "))
    if valor != 0:
        historico.append(valor)
i = 0
while i < len(historico):
    if historico[i] < 5 and historico[i]> -5:
        del historico[i]
    else:
        i += 1 
saldo = sum(historico)

print("\n==Resultado===")
print("Histórico Final:", historico)
print(f"Saldo final: R$ {saldo:.2f}")
        