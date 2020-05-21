import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = datetime.date.today().year - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Cateirade trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
        pessoa['anoC'] = int(input('Ano de Contratação: '))
        pessoa['salario'] = float(input('Salário: R$ '))
        pessoa['aposentar'] = 65 - pessoa['idade']
for k, v in pessoa.items():
    print(f'{k.capitalize():<12} {v:>10}')
