qtde_alunos = 5
nomes = []
notas = []
media = 0
for i in range(qtde_alunos):
    nomes.append(input(f"Nome do aluno {i+1}: "))
    notas.append(float(input(f"Nota de {nomes[i]}: ")))





print("Notas: ")
for i in range(qtde_alunos):
    if notas[i] > media:
        print(f"Parabéns {nomes[i]}! Sua nota foi {notas[i]:.1f}")