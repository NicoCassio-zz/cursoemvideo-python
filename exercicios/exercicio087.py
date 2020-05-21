m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = st = 0
for i in range(0, 3):
    for j in range(0, 3):
        m[i][j] = int(input(f'Número [{i}]x[{j}]: '))
maior = m[1][0]
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{m[i][j]}]', end='')
        if m[i][j] % 2 == 0:
            sp += m[i][j]
        if j == 2:
            st += m[i][j]
        if i == 1 and m[i][j] > maior:
            maior = m[i][j]
    print()
print(f'Soma dos pares: {sp}')
print(f'Soma da terceira coluna: {st}')
print(f'Maior da segunda linha: {maior}')
