op = 0
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
while op != 5:
    print('---------------------')
    print('  [1] Somar')
    print('  [2] Multiplicar')
    print('  [3] Maior')
    print('  [4] Novos Números')
    print('  [5] Sair')
    print('---------------------')
    op = int(input(' Opção: '))
    if op == 1:
        r = n1 + n2
    elif op == 2:
        r = n1 * n2
    elif op == 3:
        if n1 > n2:
            r = n1
        else:
            r = n2
    elif op == 4:
        n1 = int(input('Número 1: '))
        n2 = int(input('Número 2: '))
    elif op != 5:
        r = 'Opção inválida'
    print('Resultado: {}'.format(r))
