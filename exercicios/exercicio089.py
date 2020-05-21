boletim = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [s/n]')).lower()[0]
    if op == 'n':
        break
print('-' * 32)
print(f'{"BOLETIM":^32}')
print('-' * 32)
print(f'   N  {"NOME":<15} {"MÉDIAS":>10}')
print('-' * 32)
for i, a in enumerate(boletim):
    print(f'  [{i + 1}] {a[0]:<15} {a[2]:>10.1f}')
print('-' * 32)
op = int(input('Notas: ')) - 1
print(f'  {boletim[op][0]:<15} {boletim[op][1]}')
