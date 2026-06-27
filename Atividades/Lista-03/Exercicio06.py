investimento_mensal=float(input("Quanto será investido por mês? R$ "))
taxa_juros_mensal =float(input("Qual a taxa de juros mensal(1 pa 1%)? "))/100
saldo = 0
ano_atual = 1
while True:
    
    for mês in range(1 , 13):
        
        saldo += investimento_mensal
        
        saldo +=saldo*taxa_juros_mensal
        
    print(f"\nSaldo do investimento após {ano_atual} ano(s): R$ {saldo:.2f}")


    opcao=input("Deseja processar mais 1 ano? (S/N): "). upper( )
    if opcao == 'S':
        ano_atual+=1
    else:
        print("Simulação encerrada")
        break