def soma(*n):
    s = 0
    for i in n:
        s += i
    print(f'Soma: {s}')
#  Programa principal
soma(1, 2, 3)
soma(1, 2)
soma(1, 2, 3, 4, 5)
