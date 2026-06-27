valor_produto = float(input("Valor do Produto: "))
desconto = float(input("Digite o valor do desconto em porcentagem: "))
valor_desconto = (valor_produto * desconto) / 100
valor_final = valor_produto - valor_desconto
print(f"Valor_produto: R$ {valor_produto:.2f}")
print(f"desconto: % {desconto:.2f}")
print(f"valor_desconto: R$ {valor_desconto}")
print(f"Total a pagar: R$ {valor_final:.2f}")