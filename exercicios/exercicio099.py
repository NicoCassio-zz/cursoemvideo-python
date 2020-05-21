def maior(*n):
    m = 0
    c = 0
    print('Valores', end=' ')
    for i in n:
        if c == 0:
            m = i
            c = 1
        elif i > m:
            m = i
        print(i, end=' ')
    print()
    print(f'Maior: {m}')
#  Programa principal
maior(1, 2, 3, 4, 123, 123, 23, 31, 2312)
