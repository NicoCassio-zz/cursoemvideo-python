s = 0
t = 0
op = 's'
ma = 0
me = 0
while op == 's':
    n = int(input('Número: '))
    s += n
    t += 1
    op = str(input('Quer continuar? [s/n]'))
    if n > ma:
        ma = n
    if n < me:
        me = n
print('Média: {:.2f}'.format(s / t))
print('Maior: {}'.format(ma))
print('Menor: {}'.format(me))
