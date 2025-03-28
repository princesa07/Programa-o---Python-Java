quantidade_turmas = int(input("Digite a quantidade de turmas: "))
quantidade_alunos = int(input ("Informe a quantidade total de alunos: "))
media = quantidade_alunos/quantidade_turmas
if media < 40:
    print(f"A média de alunos ppr turma é: {media}")
else:
    print("ATENÇÃO: Uma das turmas tem mais de 40 alunos.")
