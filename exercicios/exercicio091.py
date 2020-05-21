import random, operator
jogo = dict()
for i in range(0, 4):
    jogo[f'jogador {i + 1}'] = random.randint(1, 6)
    print(f'Jogador {i + 1}: {jogo[f"jogador {i + 1}"]}')
print()
for i, l in enumerate(sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)):
    print(f'{i + 1}º - {l[0].capitalize()}: {l[1]}')
