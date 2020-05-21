l = list()
while True:
    n = int(input('Número: '))
    if n not in l:
        l.append(n)
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [s/n]')).lower()[0]
    if op == 'n':
        break
l.sort()
print(l)
