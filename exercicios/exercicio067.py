while True:
    n = int(input('Número: '))
    if n < 0:
        break
    print('-' * 11)
    print('  TABUADA')
    print('-' * 11)
    for i in range(1, 11):
        print(f'{n} X {i} = {n * i}')
    print('----------')
