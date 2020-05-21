n = int(input('Número: '))
d = 0
for i in range(1, n):
    if n % i == 0:
        d += 1
print('{}'.format('Primo' if d == 1 else 'Não primo'))
