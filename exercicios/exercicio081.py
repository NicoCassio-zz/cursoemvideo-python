n = list()
while True:
    n.append(int(input('Número: ')))
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [s/n]'))
    if op == 'n':
        break
print(f'Total: {len(n)}')
n.sort(reverse=True)
print(f'Decrescente: {n}')
print(f'Tem 5: {5 in n}')
