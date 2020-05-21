n = 0
i = 0
s = 0
while i != 999:
    i = int(input('Número: '))
    if i != 999:
        n += 1
        s += i
print('Soma: {}'.format(s))
print('Total: {}'.format(n))
