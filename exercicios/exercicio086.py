m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        m[i][j] = int(input(f'Número [{i}]x[{j}]: '))
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{m[i][j]}]', end='')
    print()
