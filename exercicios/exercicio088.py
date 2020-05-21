import random
jogo = list()
l = list()
n = int(input('Quantos jogos? '))
for i in range(0, n):
    for j in range(0, 6):
        jogo.append(random.randint(1, 60))
    jogo.sort()
    l.append(jogo[:])
    jogo.clear()
for i, j in enumerate(l):
    print(f'Jogo {i}: {j}')
