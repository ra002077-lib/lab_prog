def permitir_acesso(ano_nascimento):
    ano_atual = 2026
    idade = ano_atual - ano_nascimento
    return idade >= 18

ano = int(input("Digite o ano de seu nascimento: "))
if permitir_acesso(ano):
    print("Bem Vindo: Acesso Permitido!!!")
else:
    print("Acesso Bloqueado: Idade igual ou maior de 18 anos!")
