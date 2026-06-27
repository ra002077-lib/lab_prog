def verificar_status_aluno(media):
    if media > 6:
        return "Aprovado"
    elif media >= 4 and media <= 6:
        return "Verificação Supelmentar"
    else:
        return "Reprovado"

print(f"nota 7.5: {verificar_status_aluno(7.5)}")
print(f"nota 6: {verificar_status_aluno(6)}")
print(f"nota 3.9: {verificar_status_aluno(3.9)}")