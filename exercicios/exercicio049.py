n = int(input('Digite um número: '))
print('-' * 20)
print('{:^20}'.format('TABUADA'))
print('-' * 20)
for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, n * i))
print('-' * 20)
