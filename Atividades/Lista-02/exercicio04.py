import random

def jogo_adivinhacao():
    print("---Desafio Aleatório ---")
    print("Digite um número entre 1 e 20. Você tem 5 tentativas! ")
    
    numero_secreto = random.randint(1, 20)
    tentativas_maximas = 5

    for tentativa in range(1, tentativas_maximas + 1):
        try:
            palpite = int(input(f"\nTentativa {tentativa}/{tentativas_maximas} - Qual o seu palpite? "))
        except ValueError:
            print("Digite um número inteiro válido. ")
            continue
              
        if palpite == numero_secreto:
            print(f" Parabéns! Você ACERTOU! O número era {numero_secreto}.")
            break
        elif palpite > numero_secreto:
            print("Está ACIMA! (O número secreto é menor)")
        else:
            print("Está ABAIXO! (O número secreto é maior)")

 
        if tentativa == tentativas_maximas:
            print(f"\nSuas tentativas acabaram. O número era {numero_secreto}.")


jogo_adivinhacao()