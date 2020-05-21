def contador(i, f, p):
    if i > f:
        p = -p
    print(f'Contando de {i} a {f}: ')
    for c in range(i, f + 1, p):
        print(c, end='.. ')
    print()
#  Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))
