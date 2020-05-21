l = list()
lp = list()
li = list()
while True:
    l.append(int(input('Número: ')))
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [s/n] ')).lower()[0]
    if op == 'n':
        break
for i in l:
    if i % 2 == 0:
        lp.append(i)
    else:
        li.append(i)
print(f'Lista: {l}')
print(f'Lista pares: {lp}')
print(f'Lista ímpares: {li}')

