t = c = i= 0
menor = ''
while True:
    n = str(input('Nome: ')).capitalize()
    p = float(input('Preço: R$ '))
    t += p
    if i == 0:
        m = p
        menor = n
        i += 1
    if p > 1000:
        c += 1
    if p < m:
        menor = n
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [s/n]')).lower()[0]
    if op == 'n':
        break
print(f'Total: {t:.2f}')
print(f'Mais de 1000: {c}')
print(f'Mais barato: {menor}')
