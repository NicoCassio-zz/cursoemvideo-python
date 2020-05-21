s = 0
for i in range(0, 6):
    n = int(input('Número {}: '.format(i + 1)))
    if n % 2 == 0:
        s += n
print('Soma dos pares: {}'.format(s))
