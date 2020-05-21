aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] < 4:
    aluno['situacao'] = 'REPROVADO'
elif aluno['media'] < 6:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'APROVADO'
print(f'{aluno["nome"]}: {aluno["situacao"]}')
