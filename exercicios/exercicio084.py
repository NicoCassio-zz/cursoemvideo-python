d= list()
l = list()
ma = me = i = 0
while True:
    d.append(str(input('Nome: ')).title())
    d.append(float(input('Peso: ')))
    l.append(d[:])
    d.clear()
    if i == 0:
        ma = l[0][1]
        me = l[0][1]
        i += 1
    elif l[-1][1] >= ma:
        ma = l[-1][1]
    elif l[-1][1] <= me:
        me = l[-1][1]
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [s/n] ')).lower()[0]
    if op == 'n':
        break
print(f'Total de cadastros: {len(l)}')
print('PESADOS:')
for x in l:
    if x[1] == ma:
        print(f'{x[0]} - {x[1]}')
print('LEVES:')
for x in l:
    if x[1] == me:
        print(f'{x[0]} - {x[1]}')
